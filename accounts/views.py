from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        p_form = ProfileForm(request.POST)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/accounts/profile')
    else:
        form = SignupForm()
        p_form = ProfileForm
    return render(request, 'registration/signup.html', {'form': form, 'p_form': p_form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile})


