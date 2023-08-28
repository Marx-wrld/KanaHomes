from django.db import models

# Creating a db model for our categories

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta: 
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
#creating a db model for our products
class Product(models.Model):
    #foreign key
    #CASCADE so that if we delete the category we delete all of its products
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    #setting the ordering so that the newest product comes first
    class Meta: 
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name