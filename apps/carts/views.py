from django.contrib.auth.models import User
from django.http import JsonResponse
from apps.products.models import Product
from .models import Cart


def add_cart(request):
    user_email = request.GET.get('user_email')
    product = request.GET.get('product')

    user = User.objects.get(email=user_email)
    product = Product.objects.get(slug=product)

    cart = Cart.objects.get(user=user)

    if not cart:
        cart = Cart(user=user)
        cart.save()
        cart.products.add(product.id)
    else:
        cart.products.add(product.id)

    data = {'msg': 'added product'}

    return JsonResponse(data)
