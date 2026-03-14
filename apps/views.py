from django.shortcuts import render, get_object_or_404

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
