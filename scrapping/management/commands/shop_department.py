from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from apps.products.models import ShopDepartment


class Command(BaseCommand):

    def handle(self, *args, **options):

        url = requests.get('https://www.gearbest.com/')

        soup = BeautifulSoup(url.text, 'html.parser')

        results = soup.find('ul', attrs={'class': 'categories-list-box'})

        # print(results)

        cont = 0
        pk = 0
        for result in results:
            cont = cont + 1
            if cont % 2 == 0:
                print(result.find('a').text)
                pk = pk + 1
                ShopDepartment(
                    pk=pk,
                    name=result.find('a').text,
                    web_url=result.find('a')['href']
                ).save()
