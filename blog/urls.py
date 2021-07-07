from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostDetailViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet,  basename='post')
router.register(r'comments', CommentViewSet, basename='comment'),
router.register(r'posts/<int:pk>', PostDetailViewSet, basename='postdetail'),

urlpatterns = router.urls