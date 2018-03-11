from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from apps.products.models import ShopDepartment, Brand


class Command(BaseCommand):

    def handle(self, *args, **options):

        Brand.objects.all().delete()
        url_base = 'https://www.gearbest.com'
        shop_departments = ShopDepartment.objects.filter(active=True)

        pk = 0
        for shop_department in shop_departments:
            print(url_base + shop_department.web_url)
            url_shop = url_base + shop_department.web_url
            url = requests.get(url_shop)

            soup = BeautifulSoup(url.text, 'html.parser')
            results = soup.find_all('section', attrs={'class': 'block_b'})
            cont = 0
