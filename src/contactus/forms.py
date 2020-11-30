from django import forms
from .models import Contact

class ContactUsForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']


