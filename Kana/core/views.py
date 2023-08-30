from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.shortcuts import render, redirect
from product.models import Product, Category
from .forms import SignUpForm

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:8] #limiting our products so that only 8 appear on the frontpage
    return render(request, 'core/frontpage.html', {'products': products}) #appending our products so that it appears on the frontpage

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) #passing the data that the user has submitted

        if form.is_valid():
            user = form.save() #saving the user

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def login_old(request):
    return render(request, 'core/login.html')

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)
    
    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query)) #searching in both the name and description fields

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }
    return render(request, 'core/shop.html', context)