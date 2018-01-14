from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=120)


class ShopDepartment(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        ShopDepartment,
        related_name='categories',
        on_delete=models.DO_NOTHING,
    )
    image_url = models.URLField(blank=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    discounts = models.IntegerField()
    description = models.CharField(max_length=150)
    brand = models.ForeignKey(
        Brand,
        related_name='products',
        on_delete=models.DO_NOTHING,
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.DO_NOTHING,
    )


class ImageProduct(models.Model):
    url = models.URLField()
    product = models.ForeignKey(
        Product,
        related_name='image_product',
        on_delete=models.DO_NOTHING,
    )


class Publicity(models.Model):
    url = models.URLField()
    product = models.ForeignKey(
        Product,
        related_name='publicity',
        on_delete=models.DO_NOTHING,
    )
