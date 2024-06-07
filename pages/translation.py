from modeltranslation.translator import TranslationOptions, register
from pages.models import InfoModel


@register(InfoModel)
class InfoTranslationOptions(TranslationOptions):
    fields = ('name', 'profession', 'info')

