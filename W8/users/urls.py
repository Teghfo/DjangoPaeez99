
from django.urls import path

from .views import RegisterView, PrivateView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('private/', PrivateView.as_view(), name='private'),
]
