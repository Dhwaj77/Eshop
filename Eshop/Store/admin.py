from django.contrib import admin
from .models import Product, Category, Customer, Order

# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', "price", "category"]  # we can also define it in models by str method

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)


