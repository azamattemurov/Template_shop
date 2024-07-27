from modeltranslation.translator import TranslationOptions, register
from products.models import ProductModel, ProductCategoryModel, ProductManufacture, ProductColor, ProductTagModel, \
    ProductSizeModel, ProductCommentModel


@register(ProductManufacture)
class ProductManufactureTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ProductCategoryModel)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ProductTagModel)
class ProductTagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ProductSizeModel)
class ProductSizeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ProductColor)
class ProductColorTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ProductModel)
class ProductModelTranslationOptions(TranslationOptions):
    fields = ('title', 'long_description', 'short_info',)

@register(ProductCommentModel)
class ProductCommentTranslationOptions(TranslationOptions):
    fields = ('message',)
