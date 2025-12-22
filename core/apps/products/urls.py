from rest_framework import routers
from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')  

urlpatterns = [
    path('', include(router.urls)),
]