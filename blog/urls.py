from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet,  basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls