from django.contrib import admin

# Register your models here.

from .models import ShopUser, Category, Item

admin.site.register(ShopUser)
admin.site.register(Category)
admin.site.register(Item)