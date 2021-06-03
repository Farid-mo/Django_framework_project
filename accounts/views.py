from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileUserForm, ProfileForm, EditProfileForm, EditProfileInhForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
# Create your views here.


def profile_user(request):
    data_profile = ProfileUserForm(instance=request.user.profile)
    if request.method == "POST":
        data_profile = ProfileUserForm(request.POST)
        # data_profile = data_profile
        if data_profile.is_valid():
            data_profile.save()
    else:
        data_profile = ProfileUserForm(instance=request.user.profile)
    context = {'data_profile': data_profile}
    return render(request, 'profile/prof_form.html', context)

    # return render(request, 'profile/profile_edit.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/accounts/profile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile})


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user


class UserProfileEditView(generic.UpdateView):
    form_class = EditProfileInhForm
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.Profile.user



