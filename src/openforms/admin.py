from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.OpenForm)
admin.site.register(models.SubmittedForm)
admin.site.register(models.MultiChoiceQuestion)
admin.site.register(models.MultiChoiceAnswer)
admin.site.register(models.Question)
admin.site.register(models.FileUpload)

