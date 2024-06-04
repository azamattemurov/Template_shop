from django import template

from products.models import ProductModel

register = template.Library()


@register.filter
def get_user_cart(request):
    cart = request.session.get('cart', [])
    products = ProductModel.objects.filter(pk__in=cart)


    return products


@register.filter
def in_carts(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        return True
    return False