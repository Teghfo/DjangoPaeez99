from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    rate = models.IntegerField()
    tag = models.SlugField()
    time = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=200)
    rate = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
