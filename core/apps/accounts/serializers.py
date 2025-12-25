from rest_framework import serializers
from django.contrib.auth import authenticate
from .tokens import get_tokens_for_user
from .models import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            email=data['email'], 
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid email or password")
        
        tokens = get_tokens_for_user(user)
        return {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,
            'tokens': tokens
        }

