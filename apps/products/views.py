from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Category, Product, ListWish


class ProductTemplateView(TemplateView):
    template_name = 'shop/products/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductTemplateView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=kwargs['slug'])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        product = kwargs['object']
        products_related = Product.objects.related(product.category)
        context['products_related'] = products_related
        context['product_is_added_whish_list'] = product.is_added_whish_list(user)
        return context


def index(request):
    return render(request, 'admin/layouts/base.html', {})


def add_cart(request):
    print('ddddddddddddddd')
    pass


def remove_whish_list(request):
    user_email = request.GET.get('user_email')
    product = request.GET.get('product')

    user = User.objects.get(email=user_email)
    product = Product.objects.get(slug=product)

    list_wish = ListWish.objects.filter(user=user, product=product)

    if list_wish.exists():
        list_wish.delete()

    data = {'msg': 'remove product'}

    return JsonResponse(data)


def add_whish_list(request):
    user_email = request.GET.get('user_email')
    product = request.GET.get('product')

    user = User.objects.get(email=user_email)
    product = Product.objects.get(slug=product)

    query = ListWish.objects.filter(user=user, product=product)

    if not query.exists():
        list_wish = ListWish(user=user, product=product)
        list_wish.save()

    data = {'msg': 'added product'}

    return JsonResponse(data)
