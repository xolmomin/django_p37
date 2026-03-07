from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from apps.models import Category, Product


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = 'name', 'is_active'
    change_list_template = "apps/category_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('immortal/', self.set_immortal),
            path('mortal/', self.set_mortal),
        ]
        return my_urls + urls

    def set_immortal(self, request):
        self.model.objects.all().update(is_active=True)
        self.message_user(request, "hammasi OK")
        return HttpResponseRedirect("../")

    def set_mortal(self, request):
        self.model.objects.all().update(is_active=False)
        self.message_user(request, "Hammasi atmen")
        return HttpResponseRedirect("../")


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
