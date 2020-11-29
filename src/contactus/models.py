from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    contacted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.email} -> {self.subject} at {self.contacted_at}"
