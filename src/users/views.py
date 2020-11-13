from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def register(requests):
    if requests.method == 'POST':
        form = UserRegistrationForm(requests.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(requests, f'Account Created Successfully for {username}')
            return redirect('users:login')
        else:
            messages.success(requests, f'Error Setting up the account')
    else:
        form = UserRegistrationForm()
    return render(requests, 'users/register.html', {'form':form})

def profile(requests):
    form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(requests, 'users/profile.html', context)



