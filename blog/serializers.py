from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(source = 'users.User', read_only = True, )
    class Meta:
        model = Post
        fields = ('id', 'owner', 'date', 'body')

class CommentSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Comment
        fields = ('name', 'body',)