from django.urls import path, include

from .views import Login, SignUp, logout_view, gher_umdan

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path('gher/', gher_umdan, name='gher-umadan'),
]
