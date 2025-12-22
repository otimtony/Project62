from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from django.urls import path, include

from .views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

comments_router = NestedDefaultRouter(router, r'posts', lookup='post')
comments_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(comments_router.urls)),
]