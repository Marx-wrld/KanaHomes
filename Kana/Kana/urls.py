from django.contrib import admin
from django.urls import path
from cart.views import add_to_cart
from core.views import frontpage, shop
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'), #This means that we want slug to be a dynamic part of the url, so here we expect a slug and we give it a name of slug
    path('add_to_cart/<int:product>/', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
]
