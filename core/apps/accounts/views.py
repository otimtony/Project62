from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import LoginSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class AuthViewSet(viewsets.ViewSet):
    permission_classes = []  # Allow unrestricted access

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
