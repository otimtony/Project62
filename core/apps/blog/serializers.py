from rest_framework import serializers
from .models import Post, Comment
from apps.accounts.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class PostSerializer(serializers.ModelSerializer):
    added_by = AuthorSerializer(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'added_by', 'title', 'content', 'published', 'published_at', 'created_at', 'updated_at', 'comments_count']    

class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)   
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at', 'updated_at']