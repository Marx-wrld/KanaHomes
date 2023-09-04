from django.urls import path
from django.contrib.auth import views
from core.views import frontpage, shop, signup, myaccount, edit_myaccount
from product.views import product


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'), #This means that we want slug to be a dynamic part of the url, so here we expect a slug and we give it a name of slug 
]