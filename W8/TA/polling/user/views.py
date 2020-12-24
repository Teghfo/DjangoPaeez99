from django.shortcuts import render
from django.views.generic import CreateView, FormView, RedirectView
from .forms import LoginForm, ProfileForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect


# Create your views here.


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        return redirect('login')


class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = ProfileForm
    success_url = reverse_lazy('login')


class LogoutView(RedirectView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
