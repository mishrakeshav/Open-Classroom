from django.shortcuts import render,redirect
from .forms import SubscribeForm
from .models import Subscriber
# Create your views here.

def subscribe(request):
    if request.method=='POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscriber = Subscriber.objects.create(email=form.cleaned_data.get('email'))
            return redirect('landing-page')