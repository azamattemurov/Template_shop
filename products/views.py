from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from products.models import ProductModel, ProductCategoryModel, ProductManufacture, ProductColor, ProductTagModel, \
    ProductSizeModel


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        qs = ProductModel.objects.all().order_by('-pk')
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        man = self.request.GET.get('man')
        col = self.request.GET.get('col')
        sort = self.request.GET.get('sort')
        q = self.request.GET.get('q')

        if cat:
            qs = qs.filter(categories__in=cat)
        if tag:
            qs = qs.filter(tags__in=tag)
        if man:
            qs = qs.filter(manufacture__in=man)
        if col:
            qs = qs.filter(color__in=col)
        if sort:
            if sort == '-price':
                qs = qs.order_by('-real_price')
            else:
                qs = qs.order_by('real_price')
        if sort:
            if sort == 'title':
                qs = qs.order_by('title')
            else:
                qs = qs.order_by('-title')
        if q:
            qs = qs.filter(title__icontains=q)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['categories'] = ProductCategoryModel.objects.all()
        content['manufacture'] = ProductManufacture.objects.all()
        content['color'] = ProductColor.objects.all()
        content['tags'] = ProductTagModel.objects.all()

        return content


class ProductDetailView(DetailView):
    template_name = 'products/products-detail.html'
    model = ProductModel
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['product'] = ProductModel.objects.all()
        content['tags'] = ProductTagModel.objects.all()
        content['categories'] = ProductCategoryModel.objects.all()
        content['color'] = ProductColor.objects.all()
        content['manufacture'] = ProductManufacture.objects.all()

        return content


def add_or_remove(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session['cart'] = cart
    return redirect(request.GET.get('next', 'products:list'))


def add_or_r(request, pk):
    wishlist = request.session.get('wishlist', [])
    if pk in wishlist:
        wishlist.remove(pk)
    else:
        wishlist.append(pk)
    request.session['wishlist'] = wishlist
    return redirect(request.GET.get('next', 'products:list'))





