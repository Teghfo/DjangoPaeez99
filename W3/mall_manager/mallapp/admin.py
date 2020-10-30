from django.contrib import admin

from .models import Costumer, Mall, Category, Comment, Store

admin.site.register(Comment)
admin.site.register(Mall)
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Costumer)
