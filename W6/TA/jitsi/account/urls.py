from django.urls import path

from .views import signup, joinoradd_team, login_account, logout_account, exit_team, JoinOrAddTeam
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('team/', joinoradd_team, name='team'),
    path('team-class/', login_required(JoinOrAddTeam.as_view()), name='team-class'),
    path('logout/', logout_account, name='logout'),
    path('login/', login_account, name='login'),
    path('exit_team/', exit_team, name='exit')
]
