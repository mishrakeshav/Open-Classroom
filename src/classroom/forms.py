from django.forms import ModelForm
from django import forms
from  .models import Classroom


class ClassroomCreationForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'description']

class JoinClassroomForm(forms.Form):
    code = forms.CharField(label='Enter Code', max_length=100)


