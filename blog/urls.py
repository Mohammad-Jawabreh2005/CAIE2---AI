
from django.urls import include, path
from rest_framework import routers

from .views import (
    CategoryViewSet,
    CommentViewSet,
    PostViewSet,
    UserViewSet,
    get_posts,
)

router = routers.DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('posts/get_posts/', get_posts, name='get_posts'),
    path('', include(router.urls)),
]
