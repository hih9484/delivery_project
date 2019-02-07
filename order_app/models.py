from django.db import models
from store_app.models import Menu


# Create your models here.
class Basket(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    #user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
