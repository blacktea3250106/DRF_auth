from django.contrib.auth.models import User
from rest_framework import serializers, validators

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "email":{
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that Email already exists"
                    )
                ]
            }
        }
 
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')

        user = User.objects.create_user(username=username, email=email) 

        user.set_password(password) # Hashing and setting the user's password securely.
        user.save()

        return user
