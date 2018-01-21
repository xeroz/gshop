from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from apps.products.models import ShopDepartment


class Command(BaseCommand):

    def handle(self, *args, **options):
        shop_departments = ShopDepartment.objects.all()

        for shop_department in shop_departments:
            print(shop_department.name, '############')
            for category in shop_department.categories.all():
                print(category.name)
                print(category.web_url)
                print('000000000000000000')
                url = requests.get(category.web_url)
                soup = BeautifulSoup(url.text, 'html.parser')

                products = soup.find_all('li', attrs={'class', 'c_cate'})

                for product in products:
                    product_name = product.find('p', attrs={'class', 'all_proNam'}).find('a').text
                    product_image = product.find('p', attrs={'class', 'all_proImg'}).find('a').find('img')['data-original']
                    product_url = product.find('p', attrs={'class', 'all_proImg'}).find('a')['href']
                    product_price = product.find('div', attrs={'class', 'all_price'}).find('span', attrs={'class', 'my_shop_price'}).text
                    print (product_url)

                    url_detail = requests.get(product_url)
                    detail = BeautifulSoup(url_detail.text, 'html.parser')

                    try:
                        product_brand = detail.find('a', attrs={'class', 'brand-name'}).text
                    except Exception:
                        product_brand = ''

                    print(product_brand)

                    print('11111111111111111111111')
