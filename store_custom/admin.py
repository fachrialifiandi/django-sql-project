from django.contrib import admin
from store.admin import ProductAdmin
from store.models import Product    
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TaggedItem


class TaginLine(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
    
class CustomProductAdmin(ProductAdmin):
    inlines = [TaginLine]
    
admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)