from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from products.forms import ProductsCommentModelForm
from products.models import ProductModel, ProductCategoryModel, ProductManufacture, ProductColor, ProductTagModel, \
    ProductSizeModel, ProductCommentModel


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
        product = ProductModel.objects.get(id=self.kwargs['pk'])
        content = super().get_context_data(**kwargs)
        content.update({
            'categories': ProductCategoryModel.objects.all(),
            'manufacture': ProductManufacture.objects.all(),
            'color': ProductColor.objects.all(),
            'tags': ProductTagModel.objects.all(),
            'product': ProductModel.objects.all(),
            'comments': ProductCommentModel.objects.filter(product=product),
        })

        return content


def add_or_remove(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session['cart'] = cart
    return redirect(request.GET.get('next', 'products:list'))


class ProductCommentView(LoginRequiredMixin, CreateView):
    template_name = 'products/products-detail.html'
    form_class = ProductsCommentModelForm
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        product_id = self.kwargs['pk']
        product = ProductModel.objects.get(pk=product_id)
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.product = product
        comment.save()
        return self.get_success_url()

    def form_invalid(self, form):
        return self.get_success_url()

    def get_success_url(self):
        return redirect(self.request.GET.get('next', 'products:list'))
