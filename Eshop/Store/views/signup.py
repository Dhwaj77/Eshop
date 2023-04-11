from django.shortcuts import render, redirect
from django.http import HttpResponse
from Store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postdata = request.POST
        firstname = postdata.get('firstname')
        lastname = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        # validation
        value = {"firstname": firstname, "lastname": lastname,
                    "phone": phone, "email": email, "password": password}

        customer = Customer(firstname=firstname, lastname=lastname,
                            phone=phone, email=email, password=password)
        
        error_msg = self.validatecustomer(customer)
        
        if not error_msg:
            print(firstname, lastname, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            # or
            # customer.save()   if there is no register method
            return redirect('homepage')
        else:
            data = {"error": error_msg, "values": value}
            return render(request, "signup.html", data)
    
    def validatecustomer(self, customer):

        error_msg = None
        if not customer.firstname:
            error_msg = "Name required..!"
        elif len(customer.firstname) < 4:
            error_msg = 'Name should have 4 char'
        elif not customer.lastname:
            error_msg = "last name required..!"
        elif len(customer.lastname) < 4:
            error_msg = "Last name should have atleast 4 char"
        elif not customer.phone:
            error_msg = "Phone is required..!"
        elif len(customer.phone) < 10 or len(customer.phone) > 10:
            error_msg = "phone length should be 10"
        elif not customer.email:
            error_msg = "Email is required..!"
        elif len(customer.email) < 5:
            error_msg = "Email length should not less than 6"
        elif not customer.password:
            error_msg = "Password is required..!"
        elif len(customer.password) < 6:
            error_msg = "Password length should not less than 6"
        elif customer.isExists():
            error_msg = "Email Address already registered..!"
        return error_msg
        # saving
