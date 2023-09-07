from django.contrib.auth.models import User
from django.db import models
from itertools import product
from product.models import Product

# Create your models here.
class Order(models.Model):
    ORDERED = 'ordered' #this section is stored in the database
    SHIPPED = 'shipped'

    STATUS_CHOICES = ( #this section is displayed in the admin interface
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
    )

    user = models.ForeignKey(User, related_name="orders", blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    #each time an order is created the time is filled automatically
    created_at = models.DateTimeField(auto_now_add=True)
    
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ['-created_at',]

#Adding a separate class for order items
class OrderItem(models.Model):
    #referencing the order in which this item belongs to
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)