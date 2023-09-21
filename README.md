# DRF User Authentication API

## Introduction
This documentation covers the API endpoints for user authentication, which include login, logout, registration, and user data retrieval. These are part of the RESTful services provided by Django Rest Framework and utilize tokens for authentication.

## 1. User Data Retrieval: get_user_data
<img src="screenshots/user.gif" width="960" height="480">

- Endpoint: /api/get_user_data/
- HTTP Method: GET
- Description: Retrieves the information of the authenticated user.
- Response:
  - 200 OK for successful retrieval of user information. Returns user data.
  - 400 Bad Request if the user is not authenticated.
 
```python
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
```
