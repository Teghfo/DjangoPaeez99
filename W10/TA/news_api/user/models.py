from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    news = models.ForeignKey('content.News', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
