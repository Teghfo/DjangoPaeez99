from django.contrib import admin

from . import models


admin.site.register(models.Element)
admin.site.register(models.ElementAddress)
admin.site.register(models.Category)
admin.site.register(models.SubCategory)
