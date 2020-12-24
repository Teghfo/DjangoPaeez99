from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2')


class LoginForm(Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)

