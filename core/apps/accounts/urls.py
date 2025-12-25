from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AuthViewSet

routers = DefaultRouter()
routers.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(routers.urls)),
]
