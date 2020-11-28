from django import forms
from .models import Course


class CourseCreationForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    link = forms.URLField(help_text='Enter the YT link')
    image = forms.ImageField(allow_empty_file=True)

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'link', 'image']

