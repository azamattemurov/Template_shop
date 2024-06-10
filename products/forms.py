from django import forms

from products.models import ProductCommentModel


class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductCommentModel
        fields = ['message']
