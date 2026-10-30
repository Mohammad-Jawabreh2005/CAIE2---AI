from django.db import models

# Create your models here.
class post(models.Model):
    title_id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=200)
    content= models.TextField()
    created_data= models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50]
