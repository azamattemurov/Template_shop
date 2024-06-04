from django.urls import path
from products.views import ProductListView, ProductDetailView, add_or_remove
from users.views import CartView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('cart/<int:pk>/', add_or_remove, name='add-or-remove'),

]
