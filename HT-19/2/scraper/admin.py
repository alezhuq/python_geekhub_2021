from django.contrib import admin

from .models import Ask, Show, Job, New

# Register your models here.

admin.site.register(Ask)
admin.site.register(Show)
admin.site.register(Job)
admin.site.register(New)
