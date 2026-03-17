from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from apps.models import Product


def product_list_page(request):
    context = {
        'products': Product.objects.all()
    }

    return render(request, 'apps/product-grid.html', context)


def product_detail_page(request, pk):
    product = get_object_or_404(Product, id=pk)

    context = {
        'product': product
    }

    return render(request, 'apps/product-details.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # 123 -> hashed_password

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('product_list_page')

    return render(request, 'apps/login.html')


def logout_page(request):
    logout(request)
    return redirect('product_list_page')
