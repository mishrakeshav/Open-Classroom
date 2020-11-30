from django.contrib.auth.models import User
from PIL import Image
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)
    image = models.ImageField(default = 'courses/default.jpg', upload_to='courses/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

        img = Image.open(self.image.path)
        
        if img.height > 400 or img.width > 400:
            output_size = (400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)


class FavouriteCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

