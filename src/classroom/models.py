from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Classroom(models.Model):
    name = models.CharField(max_length=200)
    classroom_code = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)



