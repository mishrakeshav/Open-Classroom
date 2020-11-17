from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

from classroom.models import Topic

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

class Assignment(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    turned_in = models.BooleanField(default = False)

class Resource(models.Model):
    files = models.FileField(upload_to='classroom/resources/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Attachment(models.Model):
    files = models.FileField(upload_to='classroom/attachments/')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

