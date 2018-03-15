from django.views.generic.base import TemplateView
from .models import BannerHome
from apps.products.models import ShopDepartment


class HomePageView(TemplateView):

    template_name = "shop/web/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['banners_home'] = BannerHome.objects.all()
        context['shop_departements'] = ShopDepartment.objects.filter(top_shop=True)
        return context
