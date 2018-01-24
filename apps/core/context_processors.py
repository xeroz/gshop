from apps.products.models import ShopDepartment, Product


def processors(request):
    shop_departments = ShopDepartment.objects.activate()

    data = {
        'shop_departments': shop_departments,
    }
    return data
