from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'image', 'price', 'category', 'slug')
    prepopulated_fields = {'slug': ('title',)} 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)