from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		# exclude = ('body', )
		fields = '__all__'

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
