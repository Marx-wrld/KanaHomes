from .cart import Cart

#making our cart available in all templates/globally
def cart(request):
    return {'cart': Cart(request)}