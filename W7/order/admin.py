from django.contrib import admin

from .models import Cart, CartItems


class CartItemInline(admin.TabularInline):
    model = CartItems


class CartAdmin(admin.ModelAdmin):
    readonly_fields = ('sum_cart', 'cart_length')
    inlines = [
        CartItemInline,
    ]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems)
