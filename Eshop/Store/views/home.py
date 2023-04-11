from django.shortcuts import render, redirect
from django.http import HttpResponse
from Store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
# Create your views here.
# print(make_password('1234'))
# print(check_password("1234", "pbkdf2_sha256$390000$Xbk2x8iL1jpVZnNA8gM343$TTIjVoB6C/NJu43TZ5vo/8y2PrMbcXNWRN7naaYrhIA="))

class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)

        else:
            products = Product.get_all_products()

        data = {'products': products, "categories": categories}
        # print(products)
        # return render(request, "orders/order.html")
        print('you are:-', request.session.get('email'))
        return render(request, "index.html", data)
    
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')






