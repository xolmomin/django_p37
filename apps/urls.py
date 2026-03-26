from django.urls import path

from apps.views import ProductListView, ProductDetailView, CustomLoginView, CustomLogoutView, RegisterCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_page'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product_detail_page'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('register', RegisterCreateView.as_view(), name='register_page'),
    path('logout', CustomLogoutView.as_view(), name='logout_page'),
]
