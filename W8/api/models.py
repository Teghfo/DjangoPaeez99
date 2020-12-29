from django.conf import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ba sen {self.age}"


class Pooldar(models.Model):
    aghazadeh = models.CharField(max_length=50, default='m.r')

    def __str__(self):
        return self.aghazadeh


class Publication(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        Pooldar, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
