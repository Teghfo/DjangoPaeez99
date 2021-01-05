from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', related_query_name='product')
