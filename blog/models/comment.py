
from django.db import models

from .post import Post
from .user import User


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(
    Post,
    on_delete=models.CASCADE,
    related_name='comments',
    null=True,
    blank=True
)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.content[:50]
