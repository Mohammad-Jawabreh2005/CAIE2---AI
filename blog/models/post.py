from django.db import models

from .user import User
from .category import Category

# Create your models here.
class Post(models.Model):
    title_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name="posts" , null = True , blank=True)
    categories = models.ManyToManyField(Category, related_name="posts" , blank=True)

    def __str__(self):
        return self.title