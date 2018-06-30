from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Sum
from apps.products.models import Product
from .models import Cart


class CartTemplateView(TemplateView):
    template_name = 'shop/users/cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartTemplateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['active_cart'] = True
        context['cart'] = Cart.objects.get(user=user)
        context['products'] = Cart.objects.filter(user=user).aggregate(subtotal=Sum('products__price'))

        return context


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
