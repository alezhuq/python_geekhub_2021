from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Item(models.Model):
    price = models.DecimalField(max_digits=9, decimal_places=2)
    name = models.CharField(max_length=40)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.TextField(max_length=40)
    def __str__(self):
        return self.name


class ShopUser(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username
