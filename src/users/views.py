from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import User,Profile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.filter(username=username).first()
            Profile.objects.create(user=user)
            messages.success(request, f'Account Created Successfully for {username}')
            return redirect('users:login')
        else:
            messages.success(request, f'Error Setting up the account')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(data=request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(data=request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save(commit=False)
            profile = request.user.profile
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.save()
            messages.success(request, f"Profile Updated !")
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/profile.html', context)

