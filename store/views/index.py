from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from django.views import View


class Index(View):
    def get(self,request):
        

        products=None
        categories=Category.get_all_categories()
        category_id=request.GET.get('category')
        if(category_id):
            products=Product.get_products_by_id(category_id)
        else:
            products=Product.get_all_products()
            

        return render(request,'index.html',{'products':products,'categories':categories})

    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1

                
            else:
                cart[product]=1

            
        else:
            cart={}
            cart[product]=1

        request.session['cart']=cart
        print("cart",request.session['cart'])
        return redirect('index')


