from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Assignment)
admin.site.register(models.Resource)
admin.site.register(models.Attachment)
admin.site.register(models.SubmittedAssignment)
admin.site.register(models.AssignmentFile)
