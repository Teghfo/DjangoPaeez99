from django.db import models
from django.contrib.auth.models import User

from geolocation.models import Address


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    phone = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def number_address(self):
        return len(self.address.all())

    def save(self, *args, **kwargs):
        if not self.phone:
            raise ValueError("telephon lazeme!")
        if not self.user:
            user_obj = User.objects.create(username=self.phone)
            self.user = user_obj
        return super(Profile, self).save(*args, **kwargs)


class UserAddress(Address):
    user = models.ForeignKey(
        Profile, related_name='address', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.username} - priority: {self.priority_address}"
