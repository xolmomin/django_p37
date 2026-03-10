# from django.shortcuts import render, get_object_or_404, redirect
#
# from apps.models import Product, Category
#
#
# def product_list_page(request):
#     context = {
#         'products': Product.objects.all()
#     }
#     return render(request, 'apps/product-list.html', context)
#
#
# def product_add_page(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         description = request.POST.get('description')
#         category = request.POST.get('category')
#
#         Product.objects.create(
#             name=name,
#             price=price,
#             description=description,
#             category_id=category
#         )
#         return redirect('product_list_page')
#
#     context = {
#         'categories': Category.objects.all()
#     }
#     return render(request, 'apps/product-add.html', context)
#
#
# def product_detail_page(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     context = {
#         'product': product
#     }
#     return render(request, 'apps/product-detail.html', context)
#
#
# def product_delete_page(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     product.delete()
#     return redirect('product_list_page')
