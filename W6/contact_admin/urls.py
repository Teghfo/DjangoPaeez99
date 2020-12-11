from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='comment-contact'),
]
