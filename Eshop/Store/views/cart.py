from django.shortcuts import render, redirect
from django.http import HttpResponse
from Store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from Store.models import Product
class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})
    