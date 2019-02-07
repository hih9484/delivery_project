from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Store(models.Model):
    img = models.ImageField()
    name = models.CharField(blank=False, max_length=50)
    address = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return self.name


#    @property
#    def menu(self):
#        return self.menu_set.filter(store=self)


class Menu(models.Model):
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    img = models.ImageField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name



