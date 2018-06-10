from django.db import models
from .managers import ShopDepartmentManager, ProductManager
from uuslug import uuslug
from django.urls import reverse
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User


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
    top_shop = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(ShopDepartment, self).save(*args, **kwargs)

    def get_top_category(self):
        return self.categories.filter(top_category=True)

    def offers_add_active(self):
        return self.offer_ads.filter(active=True)


class OfferAd(models.Model):
    url = models.CharField(blank=True, max_length=350)
    image = models.URLField(blank=True)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(
        ShopDepartment,
        related_name='offer_ads',
        on_delete=models.DO_NOTHING,
    )


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
    description = models.CharField(max_length=150, blank=True)
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
    slug = models.SlugField(blank=True)
    web_url = models.URLField(blank=True)
    objects = ProductManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def is_added_whish_list(self, user):
        querys = self.users.all()
        if querys.exists():
            for query in querys:
                if query.user == user:
                    valid = True
                else:
                    valid = False
        else:
            valid = False
        return valid


class DescriptionProduct(models.Model):
    content = FroalaField()
    product = models.OneToOneField(
        Product,
        related_name='descripcion_product',
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
        Category,
        related_name='publicity',
        on_delete=models.DO_NOTHING,
    )


class ListWish(models.Model):
    user = models.ForeignKey(
        User,
        related_name='products',
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        related_name='users',
        on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
