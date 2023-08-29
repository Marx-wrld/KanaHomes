from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.
def product(request, slug): #we want to also accept a slug and then get a product from the db based on the product we're on
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product.html', {'product': product})