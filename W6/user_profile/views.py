from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm
from .forms import CustomUserCreationForm


class Login(View):
    def get(self, request):
        if request.user:
            pass
            # logout(request)
            # return redirect('/')
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')


class SignUp(View):
    def get(self, request):
        form = CustomUserCreationForm()
        context = {
            'form': form
        }

        return render(request, 'signup.html', context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CustomUserCreationForm()
        return render(request, 'signup.html', context)
