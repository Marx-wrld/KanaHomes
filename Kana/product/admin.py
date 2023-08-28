from django.contrib import admin

# Registering our category db model inside admin interface
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)