from django.urls import path

from .views import show_mall

urlpatterns = [
    path('show', show_mall)
]
