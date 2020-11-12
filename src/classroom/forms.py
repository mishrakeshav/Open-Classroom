from django.forms import ModelForm
from  .models import Classroom


class ClassroomCreationForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'description']

