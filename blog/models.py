from django.db import models

class Post(models.Model):
	title=models.CharField(max_length=200)
	body= models.TextField()
	create_date = models.DateTimeField()
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	content = models.TextField()
	create_date = models.DateTimeField()
	