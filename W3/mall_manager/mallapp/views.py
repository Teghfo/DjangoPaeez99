from django.shortcuts import render
from django.http import HttpResponse


def show_mall(request):
    return HttpResponse("hello ashkan")
