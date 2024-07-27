from django import forms

from products.models import ProductCommentModel


class ProductsCommentModelForm(forms.ModelForm):
    class Meta:
        model = ProductCommentModel
        fields = ['message']
