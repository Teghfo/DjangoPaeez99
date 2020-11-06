from django.db import models


class Mall(models.Model):
    """
    Mall Data
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    category stores in mall
    """
    CATEGORYNAME = [
        ("R", 'Restaurant'),
        ("K", 'Kafsh Forushi'),
        ("L", 'Lebas Forushi'),
        ("S", 'Shokolat Forushi'),
        ("H", 'Hyper')
    ]
    category = models.CharField(
        unique=True, choices=CATEGORYNAME, max_length=1)

    def __str__(self):
        return self.category


class Store(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    mall = models.ForeignKey(Mall, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='stores/', null=True, blank=True)

    def __str__(self):
        return self.name


class Costumer(models.Model):
    username = models.CharField(
        'نام کاربری', help_text='نامت را به من بگو', error_messages={'null': 'شاملو نمیخونیا. شایدم توجه بهم نمیکنی!', 'blank': 'شاملو نمیخونیا. شایدم توجه بهم نمیکنی!'}, max_length=100, unique=True)
    purchase = models.CharField(max_length=100, null=True, blank=True)
    esm_shab = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.username


class Comment(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.comment[:20]
