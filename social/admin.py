from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'post_date', 'author')
    search_fields = ['title', 'author__username']
    list_filter = ('post_date',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment_date', 'author')
    search_fields = ['content', 'author__username']
    list_filter = ('comment_date',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
