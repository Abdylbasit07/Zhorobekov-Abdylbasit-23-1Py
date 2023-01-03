from django.shortcuts import render, redirect
from products.models import Product, Review, Category
from products.forms import ProductCreateForm, ReviewCreateForm

# Create your views here.

def main_view(request):
    return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id', default = 0))
        if category_id:
            products = Product.objects.filter(categories__in=[category_id])

        else:
            products = Product.objects.all()

        return render(request, 'products/products.html', context={
            'products': products,
            'user': None if request.user.is_anonymous else request.user
        })

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        data = {
            'product': product,
            'review': product.review.all(),
            'categories': product.categories.all(),
            'review_form': ReviewCreateForm
        }
        return render(request, 'products/detail.html', context=data)

    if request.method == 'POST':
        product = Product.objects.get(id=id)

        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                author = request.user,
                product_id=id,
                comments=form.cleaned_data.get('comments')
            )
            return redirect(f'/products/{id}/')
        else:
            return render(request, 'products/detail.html', context={
                'product': product,
                'review': product.review.all(),
                'categories': product.categories.all(),
                'review_form': form
            })

def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        data = {
            'categories': categories
        }

        return render(request, 'categories/index.html', context=data)


def product_create_view(request):
    if request.method == 'GET':
        return render(request, 'products/create.html', context={
            'form': ProductCreateForm
        })
    
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                author=request.user,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                commentable=form.cleaned_data.get('commentable', True)
            )

            return redirect('/products/')

        else:
            return render(request, 'products/create.html', context={
                'form': form
            })