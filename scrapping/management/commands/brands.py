from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from apps.products.models import ShopDepartment, Brand


class Command(BaseCommand):

    def handle(self, *args, **options):

        url_base = 'https://www.gearbest.com'
        shop_departments = ShopDepartment.objects.all()

        pk = 0
        for shop_department in shop_departments:
            print(url_base + shop_department.web_url)
            url_shop = url_base + shop_department.web_url
            url = requests.get(url_shop)

            soup = BeautifulSoup(url.text, 'html.parser')
            results = soup.find_all('section', attrs={'class': 'block_b'})
            cont = 0

            for result in results:
                label = result.find('h4').text
                if label == 'Brand':
                    brands = result.find('ul')
                    for brand in brands:
                        cont = cont + 1
                        if cont % 2 == 0:
                            pk = pk + 1
                            pp = brand.find('a')
                            pp.i.decompose()
                            brand_name = pp.text
                            print(brand_name)
                            print(brand.find('a')['href'])
                            print('###############')
                            print (pk)
                            Brand.objects.get_or_create(
                                name=brand_name,
                                defaults={
                                    'pk': pk,
                                    'name': brand_name
                                },
                            )
