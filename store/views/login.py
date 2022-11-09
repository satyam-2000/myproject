from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from django.views import View



class Login(View):
    def get(self,request):
        return render(request,'store/login.html')


    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            flag=check_password(password,customer.Password)
            if flag:
                request.session['customer']=customer.id
                request.session['bb']=customer.First_name
                
                return redirect('index')
            else:
                error_message='Invalid Email and Password'
        else:
            error_message="Invalid Email and Password !!"
            return render(request,'store/login.html',{'error':error_message})


