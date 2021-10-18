from django.contrib import admin
from showcase.models import Newsletter


# Register your models here.
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'signed_in')
    list_filter = ('email', 'signed_in')
    search_fields = ('email', )
    readonly_fields = ('signed_in',)
