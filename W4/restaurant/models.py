from django.db import models
from django.utils.translation import gettext as _

from geolocation.models import Address


class RestaurantCat(models.Model):

    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Restaurant(models.Model):
    category = models.ForeignKey(
        RestaurantCat, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    rate = models.FloatField(default=5)

    def __str__(self):
        return f"{self.id}- {self.name}"

    class Meta:
        db_table = 'restaurant'
        # verbose_name_plural = _('name')


class RestaurantAddress(Address):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}- {self.restaurant.name}"


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
