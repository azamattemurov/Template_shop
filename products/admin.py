from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(TranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('name', 'created_at')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductTagModel)
class ProductTagModelAdmin(TranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('name', 'created_at')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class ProductImageModelAdmin(admin.StackedInline):
    model = ProductImageModel

@admin.register(ProductModel)
class ProductModelAdmin(TranslationAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ('created_at',)
    inlines = [ProductImageModelAdmin]
    readonly_fields = ['real_price']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductSizeModel)
class ProductSizeAdmin(TranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('created_at',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductColor)
class ProductColorAdmin(TranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('created_at',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductManufacture)
class ProductManufactureAdmin(TranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('created_at',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductCommentModel)
class ProductCommentModelAdmin(TranslationAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('message', 'created_at')
    list_filter = ('created_at',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
