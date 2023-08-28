from django.db import models

# Creating a db model for our categories

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta: 
        ordering = ('name',)
    
    def __str__(self):
        return self.name