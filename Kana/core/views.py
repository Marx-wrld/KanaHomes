from django.shortcuts import render
from product.models import Product

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:8] #limiting our products so that only 8 appear on the frontpage
    return render(request, 'core/frontpage.html', {'products': products}) #appending our products so that it appears on the frontpage

def shop(request):
    products = Product.objects.all()
    return render(request, 'core/shop.html', {'products': products})