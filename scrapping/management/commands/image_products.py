from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from apps.products.models import Product, ImageProduct


class Command(BaseCommand):

    def handle(self, *args, **options):
        ImageProduct.objects.all().delete()
        products = Product.objects.order_by('pk')

        pk = 0
        for product in products:
            url = requests.get(product.web_url)
            print(product.name)
            print(product.web_url)
            soup = BeautifulSoup(url.text, 'html.parser')
            results = soup.find_all('ul', attrs={'class': 'js_scrollableDiv'})

            for result in results:
                imgs = result.find_all('img')
                for img in imgs:
                    image = img['data-big-img']
                    print(image, '##################')
                    pk = pk + 1
                    print(pk)
                    ImageProduct(
                        pk=pk,
                        url=image,
                        product=product
                    ).save()

            print('333333333333333333333333333333')