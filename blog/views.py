from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def get_queryset(self):
        return Post.objects.all().filter(owner = self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset =  Comment.objects.all()
    serializer_class = CommentSerializer

    
