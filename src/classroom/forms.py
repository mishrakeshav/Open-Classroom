from django.forms import ModelForm
from django import forms
from  .models import Classroom,Topic

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

class AssignmentFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class AssignmentCreateForm(forms.Form):
    def __init__(self,user,*args, **kwargs):
        super(AssignmentCreateForm, self).__init__(*args,**kwargs)
        classrooms = list(map(lambda x: x.classroom, user.classroomteachers_set.all()))
        topics = []
        self.fields['classrooms'].choices = [(str(classroom.pk),classroom.name) for classroom in classrooms]
        for classroom in classrooms:
            topics.extend(list(classroom.topic_set.all()))
        self.fields['topics'].choices = [(str(topic.pk),f"{topic.name}->{topic.classroom.name}") for topic in topics]

    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    classrooms = forms.ChoiceField()
    topics = forms.ChoiceField()
    points = forms.IntegerField(min_value=0,max_value =100)
    due_date = forms.DateTimeField()
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})) 