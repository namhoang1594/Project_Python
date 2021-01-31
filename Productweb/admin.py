from django.contrib import admin

# Register your models here.
from Productweb.models import Products
from Productweb.models import Categories

admin.site.register(Categories)
admin.site.register(Products)
