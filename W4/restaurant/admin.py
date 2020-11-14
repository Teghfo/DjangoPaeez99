from django.contrib import admin

from .models import RestaurantCat, Restaurant, RestaurantAddress, Author, Article


admin.site.register(RestaurantAddress)
admin.site.register(Restaurant)
admin.site.register(RestaurantCat)
admin.site.register(Article)
admin.site.register(Author)
