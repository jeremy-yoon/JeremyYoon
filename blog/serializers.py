from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		# exclude = ('body', )
		fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
		read_only_fields=('post',)
