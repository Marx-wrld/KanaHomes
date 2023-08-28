from django.shortcuts import render
from product.models import Product, Category

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:8] #limiting our products so that only 8 appear on the frontpage
    return render(request, 'core/frontpage.html', {'products': products}) #appending our products so that it appears on the frontpage

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }
    return render(request, 'core/shop.html', context)