from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from django.views import View



class Contact(View):
    def get(self,request):
        return render(request,'store/contact.html')





