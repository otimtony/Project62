from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.db.models import Count
from django.contrib.auth.models import User

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.annotate(comments_count=Count('comments')).all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.kwargs['post_pk']
        )

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        user = User.objects.first()  # Replace with actual user retrieval logic
        serializer.save(post=post, author=user)
