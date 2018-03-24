from django.views.generic.base import TemplateView
from .models import BannerHome
from apps.products.models import ShopDepartment
from .documents import ProductDocument


class HomePageView(TemplateView):

    template_name = "shop/web/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['banners_home'] = BannerHome.objects.all()
        context['shop_departements'] = ShopDepartment.objects.filter(top_shop=True)
        return context


class SearchResultView(TemplateView):
    template_name = 'shop/web/search_result.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        search = request.GET['search']
        print(search, '#######')

        if search:
            products = ProductDocument.search().query('match', name=search)
        else:
            products = ''

        context['products'] = products

        return self.render_to_response(context)
