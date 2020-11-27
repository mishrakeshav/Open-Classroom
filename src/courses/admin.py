from django.contrib import admin
from .models import Course, FavouriteCourse

admin.site.register(Course)
admin.site.register(FavouriteCourse)
