from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(default = datetime.now())
    no_of_likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class ContactUs(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(default = datetime.now())

    def _str_(self):
        return self.name