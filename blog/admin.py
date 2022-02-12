from django.contrib import admin
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Post, Comment


class PostAdmin(SummernoteModelAdmin):
	pass


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)