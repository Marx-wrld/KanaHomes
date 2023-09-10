from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from PIL import Image
from io import BytesIO

# Creating a db model for our categories

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta: 
        verbose_name = 'Categorie' #(s)
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
    #Adding fields to support images and thumbnails, thumbnails will be automatically saved by django when we save or try to access the image for the first time
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    #setting the ordering so that the newest product comes first
    class Meta: 
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name

    def get_display_price(self):
        return self.price / 100
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            #checking that the image is set
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                #if there's no image
                return 'https://via.placeholder.com/240x240x.jpg'
    
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
    #image has been created to the memory but we need to save it the server
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
    #getting the thumbnail from the server and returning it to this function
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

#Customer product review
class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE) # if we delete a product we also delete all of its review
    rating = models.IntegerField(default=3)
    content = models.TextField() # for the comment
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)# we want to also know who created it
    created_at = models.DateTimeField(auto_now_add=True)