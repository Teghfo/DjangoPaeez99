from django.contrib import admin

from . import models


# class ELement():
#     pass


# class Address():
#     fk = Element()


class AddressInline(admin.TabularInline):
    model = models.ElementAddress


class MenuInline(admin.TabularInline):
    model = models.MenuCat


class FoodInline(admin.TabularInline):
    model = models.Food


class MenuAdmin(admin.ModelAdmin):
    inlines = [
        FoodInline,
    ]


class ElementAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline, MenuInline,
    ]


admin.site.register(models.Element, ElementAdmin)
# admin.site.register(models.ElementAddress)
admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.MenuCat, MenuAdmin)
admin.site.register(models.Food)
admin.site.register(models.Account)
admin.site.register(models.Supplier)
admin.site.register(models.Product)
