from django.contrib import admin
from rango.models import Category, Page

class PageInline(admin.TabularInline):
    model = Page
    extra=4

class PageAdmin(admin.ModelAdmin):
    #inlines = [PageInline]
    list_display = ('title','category', 'url')


# Register your models here.
admin.site.register(Category)

admin.site.register(Page,PageAdmin)
#admin.site.register(Page,PageInline)