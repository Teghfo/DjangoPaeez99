from django.db import models
from django.utils.translation import gettext as _

from geolocation.models import Address


class Category(models.Model):

    title = models.CharField(max_length=50, unique=True)
    poster = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='sub_category')

    def __str__(self):
        return self.sub_name


class Element(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    rate = models.FloatField(default=5)

    def __str__(self):
        return f"{self.id}- {self.name}"

    class Meta:
        db_table = 'element'
        # verbose_name_plural = _('name')


class ElementAddress(Address):
    element = models.ForeignKey(
        Element, on_delete=models.CASCADE, related_name='address')
    address_txt = models.TextField(default='tehran')

    def __str__(self):
        return f"{self.id}- {self.element.name}"
