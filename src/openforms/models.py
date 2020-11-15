from django.db import models


class OpenForm(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.models.DateTimeField()

class MultiChoiceQuestion(models.Model):
    question = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()
    answer = models.IntegerField()
    openform = models.ForeignKey(OpenForm, on_delete=models.CASCADE)

class Question(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True)
    openform = models.ForeignKey(OpenForm, on_delete=models.CASCADE)

class FileUpload(models.Model):
    files = models.FileField(upload_to='classroom/fileuploads/')
    openform = models.ForeignKey(OpenForm, on_delete=models.CASCADE)



