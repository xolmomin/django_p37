from django.urls import path

from apps.views import product_list_page, product_detail_page, login_page, logout_page

urlpatterns = [
    path('', product_list_page, name='product_list_page'),
    path('product-detail/<int:pk>', product_detail_page, name='product_detail_page'),
    path('login', login_page, name='login_page'),
    path('logout', logout_page, name='logout_page'),
]
