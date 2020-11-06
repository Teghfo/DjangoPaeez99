from django.contrib import admin

from .models import RestaurantCat, Restaurant, RestaurantAddress


admin.site.register(RestaurantAddress)
admin.site.register(Restaurant)
admin.site.register(RestaurantCat)
