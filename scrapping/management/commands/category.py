from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from apps.products.models import ShopDepartment, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        url_base = 'https://www.gearbest.com'
        url = requests.get(url_base)
        soup = BeautifulSoup(url.text, 'html.parser')

        results = soup.find('ul', attrs={'class': 'categories-list-box'})

        cont = 0
        pk = 0
        for result in results:
            cont = cont + 1
            if cont % 2 == 0:
                print(result.find('a')['href'])
                shop_department_name = result.find('a').text
                category_href = result.find('a')['href']
                shop_department = ShopDepartment.objects.get(name=shop_department_name)

                print(shop_department_name)
                print(shop_department)

                url_category = requests.get(url_base + category_href)
                web = BeautifulSoup(url_category.text, 'html.parser')
                categories = web.find_all('li', attrs={'class', 'shop-category-item'})
                print(categories)

                for category in categories:
                    pk = pk + 1
                    print(category.find('a').find('p').text)
                    print(category.find('a')['href'])
                    print(category.find('img')['src'])
                    category_name = category.find('a').find('p').text
                    category_image = category.find('img')['src']
                    category_url = category.find('a')['href']

                    Category.objects.get_or_create(
                        name=category_name,
                        defaults={
                            'pk': pk,
                            'name': category_name,
                            'category': shop_department,
                            'image_url': category_image,
                            'web_url': category_url
                        },
                    )
                    print('#######################3')
