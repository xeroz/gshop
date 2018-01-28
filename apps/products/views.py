from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from .models import Category, Product


class ProductTemplateView(TemplateView):
    template_name = 'shop/products/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductTemplateView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=kwargs['slug'])
        print(context, '##############')
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('############################333')
        return context

def index(request):
    return render(request, 'admin/layouts/base.html', {})
