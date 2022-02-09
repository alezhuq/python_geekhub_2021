from django import forms


from .models import Item, ShopUser


class UserForm(forms.ModelForm):
    class Meta:
        model = ShopUser
        fields = ["username", "password"]


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["price", "name", "category"]



