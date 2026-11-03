
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Category, Comment, Post, User
from ..serializers import (
    CategorySerializer,
    CommentSerializer,
    PostSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
def get_posts(request):
    try:
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))

        if page < 1 or limit < 1:
            return Response(
                {"error": "page and limit must be positive integers"},
                status=status.HTTP_400_BAD_REQUEST
            )

        start = (page - 1) * limit
        end = start + limit

        posts = Post.objects.all()[start:end]
        serializer = PostSerializer(posts, many=True)

        return Response({
            'post': serializer.data,
            'page': page,
            'limit': limit
        })

    except ValueError:
        return Response(
            {"error": "page and limit must be valid integers"},
            status=status.HTTP_400_BAD_REQUEST
        )
