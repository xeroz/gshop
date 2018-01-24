from django.views.generic import ListView
from django.shortcuts import render
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shop/products/list.html'


def index(request):
    return render(request, 'admin/layouts/base.html', {})
