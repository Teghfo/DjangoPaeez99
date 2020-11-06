from django.db import models

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


class RestaurantAddress(Address):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}- {self.restaurant.name}"
