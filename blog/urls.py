
from django.urls import include, path
from rest_framework import routers

from .views import (
    CategoryViewSet,
    CommentViewSet,
    PostViewSet,
    UserViewSet,
    generate_post,
    get_posts,
    summarize_post_view,
)

router = routers.DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    # Existing endpoints
    path('posts/get_posts/', get_posts, name='get_posts'),
    path('posts/generate/', generate_post, name='generate_post'),

    # AI summarization endpoint
    path(
        'posts/<int:post_id>/summarize/',
        summarize_post_view,
        name='summarize_post',
    ),
    path(
        'posts/<str:post_id>/summarize/',
        summarize_post_view,
        name='summarize_post_invalid_id',
    ),

    # Existing DRF router
    path('', include(router.urls)),
]
