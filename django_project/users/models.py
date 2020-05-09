from django.db import models
from django.contrib.auth.models import User
from cities.models import City

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField(default=0)
    address = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'