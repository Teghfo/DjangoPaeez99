from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Profile, User


Gender_Choices = [('M', 'Male'), ('F', 'Female')]


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    # username.widget.attrs.update({'id': 'username', 'width': '50px'})


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['image']
