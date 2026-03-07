from django.urls import path

from apps.views import product_detail_page, product_list_page, product_delete_page, product_add_page

urlpatterns = [
    path('', product_list_page, name='product_list_page'),
    path('product/add', product_add_page, name='product_add_page'),
    path('product-detail/<int:pk>', product_detail_page, name='product_detail_page'),
    path('product-detail/<int:pk>/delete', product_delete_page, name='product_delete_page'),
]