from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ( 'product_descriptions',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_name', 'description')


@register(Contact)
class StoreTranslationOptions(TranslationOptions):
    fields = ('contact_name',)


@register(Address)
class StoreTranslationOptions(TranslationOptions):
    fields = ('address_name',)


@register(StoreMenu)
class StoreTranslationOptions(TranslationOptions):
    fields = ('menu_name',)



@register(Order)
class StoreTranslationOptions(TranslationOptions):
    fields = ('delivery_address',)



