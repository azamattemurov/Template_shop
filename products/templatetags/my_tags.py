from django import template
from django.db.models import Sum

from products.models import ProductModel

register = template.Library()


@register.filter
def get_user_cart(request):
    cart = request.session.get('cart', [])
    products = ProductModel.objects.filter(pk__in=cart)

    return products


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])


@register.filter
def get_cart_total(request):
    cart = request.session.get('cart', [])
    total = ProductModel.objects.filter(pk__in=cart).aggregate(total_price=Sum('real_price'))['total_price']
    return total if total is not None else 0

@register.filter
def get_user_wishlist(request):
    cart = request.session.get('wishlist', [])
    products = ProductModel.objects.filter(pk__in=cart)

    return products


@register.filter
def in_wishlist(product, request):
    return product.pk in request.session.get('wishlist', [])
