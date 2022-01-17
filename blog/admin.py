from django.contrib import admin
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


class PostAdmin(SummernoteModelAdmin):
	pass


admin.site.register(Post, PostAdmin)