from django.contrib import admin

# Register your models here.
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)