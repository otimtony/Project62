from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
from .views import AuthViewSet

routers = DefaultRouter()
routers.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(routers.urls)),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
