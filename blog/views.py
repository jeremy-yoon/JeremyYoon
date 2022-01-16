from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Post
from .serializers import PostSerializer
import random

@api_view(['GET'])
def index(request):
	
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    post_list = Post.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    serializer = PostSerializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post(request, id):
	post = get_object_or_404(Post, pk=id)
	serializer = PostSerializer(post)
	return Response(serializer.data)

