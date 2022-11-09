from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from django.views import View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class Orders(View):

    @method_decorator(auth_middleware)
    def get(self,request):
        customer=request.session.get('customer')
        print("hello",customer)
        orders=Order.get_orders_by_customer(customer)
        print("orders are ",orders)
        return render(request,'store/order.html',{'orders':orders})