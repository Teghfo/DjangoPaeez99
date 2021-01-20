from django.dispatch import receiver
from django.db.models.signals import post_save
import os
from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from geolocation.models import Address
from django.core.cache.utils import make_template_fragment_key
from django.core.cache import cache


class Category(models.Model):

    title = models.CharField(max_length=50, unique=True)
    poster = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('category')


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
    descriptions = models.CharField(
        max_length=250, default='توضیحات را ویرایش کنید')

    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}- {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}', allow_unicode=True)
        return super(Element, self).save(*args, **kwargs)

    class Meta:
        db_table = 'element'
        # verbose_name_plural = _('name')


class ElementAddress(Address):
    element = models.ForeignKey(
        Element, on_delete=models.CASCADE, related_name='address')
    address_txt = models.TextField(default='tehran')

    def __str__(self):
        return f"{self.id}- {self.element.name}"


class MenuCat(models.Model):
    name = models.CharField(max_length=50)
    element = models.ForeignKey(
        Element, on_delete=models.CASCADE, related_name='menu_cat')

    # class Meta:
    #     unique_together = ('name', 'element',)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'element'], name='menu cat constraint')
        ]

    def __str__(self):
        return f"{self.name} in {self.element.name}"

    # def save(self, *args, **kwargs):
    #     cat_elment_name = self.element.menu_cat.all().values('name')
    #     for elem in cat_elment_name:
    #         if self.name == elem.get('name', None):
    #             return
    #     return super().save(*args, **kwargs)


def get_upload_path(instance, filename):
    return os.path.join(f"{instance.cat_manu.element.name}", filename)


class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    rate = models.FloatField(default=5)
    poster = models.ImageField(
        upload_to=get_upload_path, null=True, blank=True)
    cat_manu = models.ForeignKey(MenuCat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}_{self.cat_manu.name}"


class Account(models.Model):
    name = models.CharField(max_length=20)


class Supplier(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name='suplier')


class Product(models.Model):
    name = models.CharField(max_length=255)
    supplier = models.ManyToManyField(Supplier)


@receiver(post_save, sender=Food)
def clear_cache(sender, instance, **kwargs):
    key = make_template_fragment_key('showFood')
    try:
        cache.delete(key)
    except Exception as e:
        raise ValueError(e)
