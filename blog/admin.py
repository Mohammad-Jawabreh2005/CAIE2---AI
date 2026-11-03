from django.contrib import admin

from .models import Category, Comment, Post, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_id', 'title', 'author')
    list_filter = ('title_id', 'title', 'author')
    search_fields = ('title_id', 'title', 'author__username')
    ordering = ('title_id', 'title', 'author')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('username',)
    readonly_fields = ('created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('content', 'author__username')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)