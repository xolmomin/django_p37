from django.contrib import admin

from apps.models import Product, Category, Tag, ProductImage


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'name', 'category', 'price'
    filter_horizontal = 'tags',
    inlines = ProductImageStackedInline,


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    list_display = 'name',
