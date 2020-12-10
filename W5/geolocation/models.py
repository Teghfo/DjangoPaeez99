from django.db import models


class TehAddressManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(city='تهران')


class Address(models.Model):
    STATE = [
        ('tehran', 'تهران'),
        ('alborz', 'البرز'),
        ('markazi', 'مرکزی'),
    ]

    state = models.CharField('استان', choices=STATE,
                             max_length=20)
    city = models.CharField('شهر', max_length=50)
    street = models.CharField('خیابان', max_length=50)
    alley = models.CharField('کوچه', max_length=50)
    number = models.CharField('پلاک', max_length=50)
    poste_code = models.CharField('کدپستی', max_length=50)
    priority_address = models.SmallIntegerField(default=1)
    location = models.CharField(
        'موقعیت جغرافیایی', max_length=50)

    objects = models.Manager()
    teh_objects = TehAddressManager()
