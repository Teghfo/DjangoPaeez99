from django.db import models
from django.contrib.auth import get_user_model

from restaurant.models import Food

User = get_user_model()


class Cart(models.Model):
    food = models.ManyToManyField(Food, through='CartItems')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    @property
    def cart_length(self):
        return self.cartitems.count()

    @property
    def sum_cart(self):
        cartitems = self.cartitems.select_related('food')
        sum_food_prices = 0
        for elm in cartitems:
            sum_food_prices += (elm.food.price * elm.qty)
        return sum_food_prices

    def __str__(self):
        return f"{self.user.email}"

    class Meta:
        permissions = [('akbar_refighemuneh', 'Akbar Can Hame Kar')]


class CartItems(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cartitems")
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'food'], name='cart item constraint')
        ]
