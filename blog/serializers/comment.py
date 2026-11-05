
from typing import ClassVar

from rest_framework import serializers

from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

        extra_kwargs: ClassVar[dict] = {
            'author': {
                'required': True,
                'allow_null': False,
            },
            'post': {
                'required': True,
                'allow_null': False,
            },
        }
