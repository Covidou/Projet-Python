from django.db import models
from users.models import User

class Product(models.Model):
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user} <- {self.quantity} * {self.product}"