from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

from openforms.models import OpenForm

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_assignment = models.BooleanField(default=False)

class Assignment(models.Model):
    pass 

class Attachment(models.Model):
    files = models.FileField(upload_to='classroom/attachments/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


