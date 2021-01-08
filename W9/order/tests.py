from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model

from restaurant.models import Food
from order.models import Cart

User = get_user_model()

# Model Test


class TestCartModel(TestCase):
    def setUp(self):
        self.user = User()
        self.food = Food()
        self.cart = Cart()

    def test_cart_user_field(self):
        user_label = self.cart._meta.get_field('user')
        self.assertIsInstance(user_label, models.OneToOneField)

    def test_cart_food_field(self):
        food_label = self.cart._meta.get_field('food')
        self.assertIsInstance(food_label, models.ManyToManyField)

    def test_cart_last_update_field(self):
        last_update_label = self.cart._meta.get_field('last_update')
        self.assertIsInstance(last_update_label, models.DateTimeField)

# View Test

# Form Test

# API Test
