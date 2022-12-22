from django.shortcuts import render
from products.models import Product, Review, Category

# Create your views here.

def main_view(request):
    return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id'))

        if category_id:
            products = Product.objects.filter(categories__in=[category_id])
        else:
            products = Product.objects.all()

        return render(request, 'products/products.html', context={
            'products': products
        })

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        data = {
            'product': product,
            'review': product.review.all(),
            'categories': product.categories.all()
        }
        return render(request, 'products/detail.html', context=data)

def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        data = {
            'categories': categories
        }

        return render(request, 'categories/index.html', context=data)