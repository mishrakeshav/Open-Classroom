from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from posts.models import Assignment

class OpenForm(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SubmittedForm(models.Model):
    openform = models.ForeignKey(OpenForm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.openform.title}"


class MultiChoiceQuestion(models.Model):
    question = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()
    answer = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ])
    openform = models.ForeignKey(OpenForm, on_delete=models.CASCADE)



class MultiChoiceAnswer(models.Model):
    question = models.ForeignKey(MultiChoiceQuestion, on_delete=models.CASCADE)
    user_answer = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ])
    form = models.ForeignKey(SubmittedForm, on_delete=models.CASCADE)


class Question(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True)
    openform = models.ForeignKey(OpenForm, on_delete=models.CASCADE)

class FileUpload(models.Model):
    files = models.FileField(upload_to='classroom/fileuploads/')
    openform = models.ForeignKey(OpenForm, on_delete=models.CASCADE)



