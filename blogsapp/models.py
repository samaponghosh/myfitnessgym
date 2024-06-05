from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from datetime import datetime
# Create your models here.

User = get_user_model()
# class Blogs(models.model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='blog_post_images')
#     caption = models.TextField()
#     created_at = models.DateTimeField(default=datetime.now)
#     no_of_likes = models.IntegerField(default=0)

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(primary_key=True, default='mygym')
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', default="admin")
    author = models.CharField(max_length=200, default="admin")
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title