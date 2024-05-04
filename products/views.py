from django.shortcuts import render, redirect
from .models import Category, Products
from .form import ProductForm
# Create your views here.

def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_products(request, pk):
    product= Products.objects.filter(category=pk)
    context = {
        'products': product
    }
    return render(request, 'products.html', context=context)

def detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)

def add_products(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('products:get_info')
    context = {
        'form': form
        }
    return render(request, 'create.html', context=context)


def update_products(request, pk):
    data = Products.objects.get(pk=pk)
    form = ProductForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('products:get_info')
    context = {
        'form': form
        }
    return render(request, 'update.html', context=context)

def delete_products(request, pk):
    data = Products.objects.get(pk=pk)
    data.delete()
    return redirect('products:get_info')

def search_products(request):
    if request.method == 'POST':
        search = request.POST['search']
        product = Products.objects.filter(name__icontains=search)
        context = {
            'products': product
        }
        return render(request, 'search.html', context=context)
    else:
        return redirect('products:get_info')