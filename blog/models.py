from django.db import models

class Category(models.Model):
	title=models.CharField(max_length=200)
	represent_image = models.ImageField(null=True, blank=True)
	

class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	# category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
	title=models.CharField(max_length=200)
	body= models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	represent_image = models.ImageField(
        upload_to="post/%Y/%m/%d", null=True, blank=True)
	update_date = models.DateTimeField(null=True, blank=True)
	view_count = models.IntegerField(default=0, verbose_name='조회수')
	like_count = models.IntegerField(default=0, verbose_name='좋아요')
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	writer = models.CharField(max_length=10, null=True, blank=True)
	content = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(null=True, blank=True)
	like_count = models.IntegerField(default=0, verbose_name='좋아요')
	