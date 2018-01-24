from django.db import models
from .managers import ShopDepartmentManager
from uuslug import uuslug
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Brand, self).save(*args, **kwargs)


class ShopDepartment(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)
    web_url = models.URLField(blank=True)
    objects = ShopDepartmentManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(ShopDepartment, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        ShopDepartment,
        related_name='categories',
        on_delete=models.DO_NOTHING,
    )
    image_url = models.URLField(blank=True)
    slug = models.SlugField(blank=True)
    web_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:list', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=200)
    discounts = models.FloatField(default=0)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=150)
    brand = models.ForeignKey(
        Brand,
        related_name='products',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.DO_NOTHING,
    )
    image = models.URLField(blank=True)


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
