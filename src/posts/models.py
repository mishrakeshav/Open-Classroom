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
    
    @property
    def content_type(self):
        return 'post'
    
    @property
    def post_comment(self):
        return list(self.comment_set.all())


class Assignment(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    marks = models.IntegerField(default=100)

    def __str__(self):
        return self.title

    def is_turnedin(self, user):
        for assignment in self.submittedassignment_set.all().filter(user=user):
            if assignment.turned_in: return True
        return False
    

    @property
    def resources(self):
        return self.attachment_set.all()
    
    @property
    def content_type(self):
        return 'assignment'
    
    @property
    def comments(self):
        return list(self.privatecomment_set.all())
    
    @property
    def submitted_assignments(self):
        return list(self.submittedassignment_set.all())
    

    @property
    def total_turned_in(self):
        ct = 0
        for assignment in self.submitted_assignments:
            ct += 1 if assignment.turned_in else 0
        print(ct)
        return ct
    
    @property
    def total_missing(self):
        print(self.topic.classroom.users.all())
        return max(len(self.topic.classroom.users.all()) - self.total_turned_in, 0)

class SubmittedAssignment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turned_in = models.BooleanField(default = False)
    grade = models.IntegerField(default=0)
    is_reviewed = models.BooleanField(default=False)
    
    @property
    def file_count(self):
        return len(self.assignmentfile_set.all())
    
    @property
    def first_file_url(self):
        return self.assignmentfile_set.first().files.url

    def __str__(self):
        return f"{self.user.username} --> {self.assignment.title}"


class AssignmentFile(models.Model):
    files = models.FileField(upload_to='classroom/assignments/')
    submitted_assignment  =  models.ForeignKey(SubmittedAssignment, on_delete=models.CASCADE)

    @property
    def filename(self):
        return os.path.split(self.files.name)[-1]
    


class Resource(models.Model):
    files = models.FileField(upload_to='classroom/resources/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    @property
    def filename(self):
        return os.path.split(self.files.name)[-1]


class Attachment(models.Model):
    files = models.FileField(upload_to='classroom/attachments/')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    @property
    def filename(self):
        return os.path.split(self.files.name)[-1]
