from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
# from .models import Profile


class SignupForm(UserCreationForm):
    adds = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'last_name', 'adds'
        ]

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.adds = self.cleaned_data["adds"]
        if commit:
            user.save()
        return user


class ProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['add', 'phone_number', 'pic_profile']

    def save(self, commit=True):
        r = super(ProfileForm, self).save(commit=False)
        r.adds = self.cleaned_data["add"]
        r.phone_number = self.cleaned_data["phone_number"]
        r.pic_profile = self.cleaned_data["pic_profile"]
        if commit:
            user.save()
        return user

#
# class ProfileChangeForm(UserChangeForm):
#     class Meta:
#         model = Profile
#         fields = ['add', 'phone_number', 'pic_profile']


class ProfileUserForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileInhForm(UserChangeForm):
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    add = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['phone_number', 'add']


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']


