from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Post
from .serializers import PostSerializer
import random

@api_view(['GET'])
def post(request, id):
	totalPosts = Post.objects.all()
	posts = random.sample(list(totalPosts), id)
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data)
