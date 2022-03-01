from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		# exclude = ('body', )
		fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
	comment_count = serializers.SerializerMethodField()
	
	class Meta:
		model = Post
		# exclude = ('body', )
		fields = '__all__'

	def get_comment_count(self, obj):
        	return Comment.objects.filter(post=obj).count()

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
		read_only_fields=('post',)
