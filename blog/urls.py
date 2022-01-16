from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import post, index

urlpatterns = [
	path("<int:id>/", post),
	path('', index),
]