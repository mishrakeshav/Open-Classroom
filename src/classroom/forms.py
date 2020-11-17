from django.forms import ModelForm
from django import forms
from  .models import Classroom

class ClassroomCreationForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'description']

class JoinClassroomForm(forms.Form):
    code = forms.CharField(label='Enter Code', max_length=100)

class PostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
