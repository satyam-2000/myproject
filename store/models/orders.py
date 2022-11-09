from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    time=models.TimeField(default=datetime.datetime.now,blank=False)
    address=models.CharField(max_length=200,default="")
    Mobile_No=models.CharField(max_length=10,default=" ")
    status=models.BooleanField(default=False)


    def placeorder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-time')
    