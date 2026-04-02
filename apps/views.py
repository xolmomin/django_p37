from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.db.models import F, Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from apps.forms import RegisterUserModelForm
from apps.models import Product, Cart, Category
from apps.tasks import send_to_email
from root.settings import EMAIL_HOST_USER


class CategoryMixin:

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductListView(CategoryMixin, ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product-grid.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = super().get_queryset()

        if _category := self.request.GET.get('category'):
            qs = qs.filter(category_id=_category)

        return qs


class ProductDetailView(CategoryMixin, DetailView):
    queryset = Product.objects.all()
    template_name = 'apps/product-details.html'


class CustomLoginView(LoginView):
    template_name = 'apps/auth/login.html'
    next_page = reverse_lazy('product_list_page')


class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('product_list_page')


class RegisterCreateView(CreateView):
    queryset = User.objects.all()
    template_name = 'apps/auth/register.html'
    form_class = RegisterUserModelForm
    success_url = reverse_lazy('product_list_page')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        send_to_email.delay(self.object.email, self.object.first_name)
        return HttpResponseRedirect(self.get_success_url())


class ShoppingCartListView(CategoryMixin, LoginRequiredMixin, ListView):
    queryset = Cart.objects.all()
    template_name = 'apps/shopping-cart.html'
    context_object_name = 'carts'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        user = self.request.user

        total_price = 0
        total_count = 0
        for cart in user.carts.all():
            total_price += cart.product.current_price * cart.quantity
            total_count += cart.quantity

        context['total_price'] = total_price
        context['total_count'] = total_count

        return context


class AddCartView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)

        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart.quantity = F('quantity') + 1
            cart.save()

        return redirect(request.META['HTTP_REFERER'])


class RemoveCartView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        Cart.objects.filter(id=pk).delete()
        return redirect('shopping_cart_page')
