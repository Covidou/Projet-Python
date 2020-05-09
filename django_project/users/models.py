from django.db import models
from django.contrib.auth.models import User
from cities.models import City

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    postal_code = models.IntegerField(default=0)
    address = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'