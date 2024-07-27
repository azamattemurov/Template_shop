from modeltranslation.translator import TranslationOptions, register
from blogs.models import BlogModel, BlogTagModel, BlogCategoryModel, AuthorModel


@register(AuthorModel)
class AuthorModelTranslation(TranslationOptions):
    fields = ('name', 'about', 'position', 'profession',)


@register(BlogTagModel)
class BlogTagModelTranslation(TranslationOptions):
    fields = ('name',)


@register(BlogCategoryModel)
class BlogCategoryModelTranslation(TranslationOptions):
    fields = ('name',)


@register(BlogModel)
class BlogModelTranslation(TranslationOptions):
    fields = ('title', 'short_info', 'content', 'category', 'tags', 'author',)
