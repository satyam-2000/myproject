from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from django.views import View

class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_order_products_by_id(list(cart.keys()))
        for product in products:
            order=Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                quantity=cart.get(str(product.id)),
                address=address,
                Mobile_No=mobile,
            )
            order.placeorder()
        request.session['cart']={}
            

        print(address,mobile,customer)
        return redirect('/store/order')
