from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Classroom(models.Model):
    name = models.CharField(max_length=200)
    classroom_code = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=300)
    slug = models.SlugField(max_length=250,unique_for_date='created_at')
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    users = models.ManyToManyField(User,related_name='users')
    
    def __str__(self):
        return f'{self.name}'
        
class Topic(models.Model):
    name = models.CharField(max_length=200)
    classroom = models.ForeignKey(Classroom,on_delete = models.CASCADE)
    



