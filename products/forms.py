from django import forms

from products.models import ProductCommentModel


<<<<<<< HEAD
class ProductCommentForm(forms.ModelForm):
=======
class ProductsCommentModelForm(forms.ModelForm):
>>>>>>> 042e58711c9a9b66549bbe4d5145d950d8f453c7
    class Meta:
        model = ProductCommentModel
        fields = ['message']
