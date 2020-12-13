from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from .forms import SignUpForm, LoginForm, TeamForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .models import Account, Team
from django.views import View


def home(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            team = request.user.team
            if team:
                context = {'team': team.name}
            else:
                context = {'team': None}
        else:
            context = {'team': None}

        return render(request, 'home.html', context=context)
    else:
        return HttpResponseNotAllowed('not allowed')


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'signup.html', context=context)

    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('team')
        return redirect('signup')

    else:
        return HttpResponseNotAllowed('not allowed')


def login_account(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context=context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')

        return redirect('login')

    else:
        return HttpResponseNotAllowed('not allowed')


def logout_account(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')
    else:
        return HttpResponseNotAllowed('not allowed')


class JoinOrAddTeam(View):

    def get(self, request):
        print(self.request)
        user = self.request.user
        print(user)
        if user.team:
            return redirect('home')
        else:
            form = TeamForm()
            context = {'form': form}
            return render(self.request, 'team.html', context=context)

    def post(self, request):
        form = TeamForm(self.request.POST)
        if form.is_valid():
            name = self.request.POST.get('name')
            user = self.request.user
            try:
                team = Team.objects.get(name=name)
            except:
                team = form.save()
                print(type(team))
                team.jitsi_url_path = 'http://meet.jit.si/'.format(team.name)
                team.save()
            user.team = team
            user.save()
        return redirect('home')


@login_required(login_url='login')
def joinoradd_team(request):
    if request.method == 'GET':
        user = request.user
        if user.team:
            return redirect('home')
        else:
            form = TeamForm()
            context = {'form': form}
            return render(request, 'team.html', context=context)
    elif request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            user = request.user
            try:
                team = Team.objects.get(name=name)
            except:
                team = form.save()
                print(type(team))
                team.jitsi_url_path = 'http://meet.jit.si/'.format(team.name)
                team.save()
            user.team = team
            user.save()
        return redirect('home')


def exit_team(request):
    if request.method == 'GET':
        user = request.user
        if user:
            user.team = None
            user.save()
        return redirect('home')
