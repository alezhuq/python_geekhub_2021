from django.contrib import admin

# Register your models here.

from .models import Category, Item, ShopUser

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ShopUser)

