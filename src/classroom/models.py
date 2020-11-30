from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# members are not teachers
class Classroom(models.Model):
    name = models.CharField(max_length=200)
    classroom_code = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=300)
    slug = models.SlugField(max_length=250,unique_for_date='created_at')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    users = models.ManyToManyField(User,related_name='users')
    
    def __str__(self):
        return f'{self.name}'


# Memebers in this table are onl the teachers 
class ClassroomTeachers(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher.username} -> {self.classroom.name}'


class Topic(models.Model):
    name = models.CharField(max_length=200)
    classroom = models.ForeignKey(Classroom,on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.classroom.name} -> {self.name}'
    



