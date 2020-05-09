from django.db import models

class City(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=5, blank='')
    def __str__(self):
        return f"{self.postal_code} {self.city.name}"
