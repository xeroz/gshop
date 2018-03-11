from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from apps.products.models import Product, DescriptionProduct


class Command(BaseCommand):

    def handle(self, *args, **options):
        DescriptionProduct.objects.all().delete()

        products = Product.objects.all()

        for product in products:
            print(product.web_url, '####################')

            url = requests.get(product.web_url)
            soup = BeautifulSoup(url.text, 'html.parser')

            result = soup.find('div', attrs={'class': 'product_pz_info'})

            try:
                print(result.text)
                content = result.text
            except Exception:
                content = ''

            DescriptionProduct(
                content=content,
                product=product,
            ).save()
