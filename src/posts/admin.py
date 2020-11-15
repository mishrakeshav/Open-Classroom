from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Assignment)
admin.site.register(models.Resources)
admin.site.register(models.Attachments)
