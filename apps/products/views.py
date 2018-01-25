from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Category


class ProductTemplateView(TemplateView):
    template_name = 'shop/products/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductTemplateView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=kwargs['slug'])
        print(context, '##############')
        return context


def index(request):
    return render(request, 'admin/layouts/base.html', {})
