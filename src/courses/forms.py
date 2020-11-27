from django import forms
from .models import Course


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'link', 'image']
