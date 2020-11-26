import os 

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

    def __str__(self):
        return self.title
    
    @property
    def resources(self):
        return self.resource_set.all()

class Assignment(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def resources(self):
        return self.attachment_set.all()

class SubmittedAssignment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turned_in = models.BooleanField(default = False)
    
    def __str__(self):
        return f"{self.user.username} --> {self.assignment.title}"


class AssignmentFile(models.Model):
    files = models.FileField(upload_to='classroom/assignments/')
    submitted_assignment  =  models.ForeignKey(SubmittedAssignment, on_delete=models.CASCADE)

    @property
    def filename(self):
        return self.files.name[10:]
    


class Resource(models.Model):
    files = models.FileField(upload_to='classroom/resources/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    @property
    def filename(self):
        return self.files.name[20:][:7]


class Attachment(models.Model):
    files = models.FileField(upload_to='classroom/attachments/')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    @property
    def filename(self):
        return self.files.name[20:][:7]
