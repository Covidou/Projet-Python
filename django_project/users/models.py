from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code_postal = models.IntegerField(default=0)
    ville = models.CharField(max_length=100, blank=True)
    addresse = models.CharField(max_length=100, blank=True)
    num_tel = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
