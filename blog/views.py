from django.shortcuts import render
from .models import *
# Create your views here.


def all_posts(request):
    all_products = Product.objects.all()

    return render(request, 'blog/products.html', {'products': all_products})
    #, {'products': all_products}


def post(request, pk):
    post = Product.objects.get(id=pk)
    return render(request, 'blog/post.html', {'post': post})