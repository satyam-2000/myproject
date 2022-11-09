from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from django.views import View


class Signup(View):
    def get(self,request):
        return render(request,'store/signup.html')

    def post(self,request):
            first_name=request.POST.get('firstname')
            last_name=request.POST.get('lastname')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            password=request.POST.get('password')
            error_message=None

            value={'First_name':first_name,'Last_name':last_name,'Phone':mobile,    'Password':password ,'Email':email}

            customer=Customer(First_name=first_name,Last_name=last_name,Email=email,    Password=password,Phone=mobile)

            
            def validation(customer):
                error_message=None
                if not customer.First_name:
                    error_message="First name required."
                elif len(customer.First_name)<4:
                    error_message="First name should possess minimum 4 character"
                elif not customer.Last_name:
                    error_message="Last name required."
                elif len(customer.Last_name)<4:
                    error_message="Last name should possess minimum 4 character"
                elif not customer.Password:
                    error_message="Password Required"
                elif len(customer.Password)<8:
                    error_message="Password should possess more than 8 characters"
                elif customer.isExist():
                    error_message="Email Already Registered"
                return error_message

            error_message=validation(customer)

            if not error_message:
                customer.Password=make_password(customer.Password)
                customer.register()
                return redirect('index')

            else:

                data={
                    'values':value,
                    'error':error_message,
                }
                return render(request,'store/signup.html',data)
                    

