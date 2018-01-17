from apps.products.models import ShopDepartment


def processors(request):
    shop_departments = ShopDepartment.objects.all()

    data = {
        'shop_departments': shop_departments,
    }

    return data
