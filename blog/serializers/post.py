
from typing import ClassVar

from rest_framework import serializers

from ..models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('title_id',)

        extra_kwargs: ClassVar[dict] = {
            'author': {
                'required': True,
                'allow_null': False,
            }
        }
