from django.contrib import admin

from . import models


# class ELement():
#     pass


# class Address():
#     fk = Element()


class AddressInline(admin.TabularInline):
    model = models.ElementAddress


class ElementAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
    ]


admin.site.register(models.Element, ElementAdmin)
# admin.site.register(models.ElementAddress)
admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.MenuCat)
admin.site.register(models.Food)
admin.site.register(models.Account)
admin.site.register(models.Supplier)
admin.site.register(models.Product)
