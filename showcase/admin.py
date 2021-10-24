from django.contrib import admin
from showcase.models import Products, Newsletter


# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'promotion', 'discontinued')
    list_filter = ('name', 'value', 'promotion', 'discontinued')
    search_fields = ('name', )
    readonly_fields = ('registered_in', )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'signed_in')
    list_filter = ('email', 'signed_in')
    search_fields = ('email', )
    readonly_fields = ('signed_in',)
