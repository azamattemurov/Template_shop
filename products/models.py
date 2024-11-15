from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategoryModel(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class ProductTagModel(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class ProductColor(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=7)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class ProductSizeModel(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class ProductManufacture(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True, upload_to='logo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('manufacture')
        verbose_name_plural = _('manufactures')


class ProductModel(models.Model):
    objects = None

    image = models.ImageField(upload_to='products/')
    image1 = models.ImageField(upload_to='products/')

    title = models.CharField(max_length=100, db_index=True)
    short_info = models.CharField(max_length=200)
    long_description = models.TextField(default="")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    sku = models.CharField(max_length=10, unique=True)
    count = models.PositiveIntegerField()
    real_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    manufacture = models.ForeignKey(ProductManufacture, on_delete=models.CASCADE, related_name='products')
    color = models.ManyToManyField(ProductColor, related_name='products')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    categories = models.ManyToManyField(ProductCategoryModel, related_name='products')
    sizes = models.ManyToManyField(ProductSizeModel, related_name='sizes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0

    def is_available(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.discount * self.price / 100

    def get_related_products(self):
        return ProductModel.objects.filter(categories__in=self.categories.all()).exclude(pk=self.pk).distinct()[:3]

    class Meta:
        ordering = ['title']
        verbose_name = _('product')
        verbose_name_plural = _('products')


class ProductImageModel(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = _('image')
        verbose_name_plural = _('images')


UserModel = get_user_model()


class ProductCommentModel(models.Model):
    objects = None
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
