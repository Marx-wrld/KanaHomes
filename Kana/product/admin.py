from django.contrib import admin

# Registering our category db model inside admin interface
from .models import Category

admin.site.register(Category)