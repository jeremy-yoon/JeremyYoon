from re import I
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
import random

@api_view(['GET'])
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    post_list = Post.objects.order_by('-create_date')
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    serializer = PostSerializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	serializer = PostSerializer(post)
	return Response(serializer.data)

@api_view(['GET'])
def comment_list(request) :
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def comment_detail(request, comment_pk):
    comments = get_list_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comments)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def comment_create(request, post_pk):
    request_method = request.method

    if request_method == 'POST':

        post = get_object_or_404(Post, pk=post_pk)
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post)

    else:
        post = get_object_or_404(Post, pk=post_pk)
        queryset = Comment.objects.filter(post=post)
        serializer = CommentSerializer(queryset, many=True)
    
    return Response(serializer.data)
    

# @api_view(['POST'])
# def comment_create(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.create_date = timezone.now()
#             comment.post = post
#             comment.save()
#             return redirect('connect:detail', post_id=post.id)
#     else:
#         form = CommentForm()
#     context = {'post': post, 'form': form}
#     return render(request, 'connect/post_detail.html', context)