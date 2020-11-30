from django.forms import ModelForm
from django import forms

class GradeStudentForm(forms.Form):
    grade = forms.IntegerField(min_value=0,max_value =100)

