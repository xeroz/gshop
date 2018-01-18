from apps.products.models import ShopDepartment


def processors(request):
    shop_departments = ShopDepartment.objects.filter(active=True)

    data = {
        'shop_departments': shop_departments,
    }
    return data
