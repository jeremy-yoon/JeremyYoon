from blog import views
from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import category_list, post, index, comment_list, comment_detail, comment_create

urlpatterns = [
	path("category/", category_list),
	path("<int:post_pk>/", post),
	path("<int:post_pk>/comments/", comment_create),
	path("comment/", comment_list),
	path("comment/<int:comment_pk>", views.comment_detail),
	path('', index),
]