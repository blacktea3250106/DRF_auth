from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from users.serializers import RegisterSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer

@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        user_data = {
            'user_info':{
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
        }

        return Response(user_data, status=status.HTTP_200_OK)

    return Response({'error': 'not authenticated'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token, _ = Token.objects.get_or_create(user=user)

    user_data = {
        'user_info':{
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'token': token.key
    }

    return Response(user_data)

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, _ = Token.objects.get_or_create(user=user)
    # token = Token.objects.create(user=user)


    user_data = {
        'user_info':{
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'token': token.key
    }

    return Response(user_data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_api(request):
    request.auth.delete() 
    return Response(status=status.HTTP_200_OK)