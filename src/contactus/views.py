from django.shortcuts import render,redirect,HttpResponse
from .forms import ContactUsForm
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(content="Message Sent",status=201)
    return HttpResponse(content="<p>Error sending message</p>")
    