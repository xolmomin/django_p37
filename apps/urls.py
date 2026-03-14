from django.urls import path

from apps.views import product_list_page, product_detail_page

urlpatterns = [
    path('', product_list_page, name='product_list_page'),
    path('product-detail/<int:pk>', product_detail_page, name='product_detail_page'),
]
