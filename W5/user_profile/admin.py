from django.contrib import admin

from .models import Profile, UserAddress

admin.site.register(Profile)
admin.site.register(UserAddress)
