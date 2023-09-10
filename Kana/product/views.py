from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Review

# Create your views here.
def product(request, slug): #we want to also accept a slug and then get a product from the db based on the product we're on
    product = get_object_or_404(Product, slug=slug)

    #checking if ou request is POST
    if request.method == 'POST':
        rating = request.POST.get('rating')
        content = request.POST.get('content')

        #checking if this form has been filled out
        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)

            #Adding security so that one user should not be able to create multiple
            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:

                review = Review.objects.create(
                    product=product,
                    rating = rating,
                    content=content,
                    created_at=request.user
                ) #redirecting back to products

            return redirect('product', slug=slug)

    return render(request, 'product/product.html', {'product': product})