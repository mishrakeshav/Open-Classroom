from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


from posts.models import Post, Assignment

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.post.title} -> {self.user.username} ({self.pk})'


class PrivateComment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.assignment.title} -> {self.user.username} ({self.pk})'

