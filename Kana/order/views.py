from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import OrderItem, Order

# Create your views here.
def start_order(request):
    cart = Cart(request)

    #checking that the form has been submitted
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        place = request.POST.get('place')
        phone = request.POST.get('phone')

    #next step is creating a new order
        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place, phone=phone)
    
    #looping through the items in the cart
        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
    
    #redirecting the user back to myaccount page
        return redirect('myaccount')
    
    #if its not a POST request we redirect the user back to the cart page
    return redirect('cart')