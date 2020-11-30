from django.contrib import admin
from .models import Comment, PrivateComment

admin.site.register(Comment)
admin.site.register(PrivateComment)