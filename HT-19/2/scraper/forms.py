from django.forms import ModelForm

from .models import Choice


class MyChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['name']
