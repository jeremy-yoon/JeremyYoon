from django.db import models

class Post(models.Model):
	title=models.CharField(max_length=200)
	body= models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	represent_image = models.ImageField(null=True, blank=True)
	update_date = models.DateTimeField(null=True, blank=True)
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	content = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(null=True, blank=True)
	