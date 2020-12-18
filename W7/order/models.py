from django.db import models
from django.contrib.auth import get_user_model

from restaurant.models import Food

User = get_user_model()


class Cart(models.Model):
    food = models.ManyToManyField(Food, through='CartItems')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}"


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'food'], name='cart item constraint')
        ]
