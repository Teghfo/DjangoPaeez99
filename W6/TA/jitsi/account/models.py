from django.contrib.auth.models import AbstractUser
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=20)
    jitsi_url_path = models.CharField(max_length=100)


class Account(AbstractUser):
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
