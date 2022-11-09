from django.db import models


class Customer(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Phone=models.CharField(max_length=15)
    Email=models.EmailField(default='hello@gmail.com')
    Password=models.CharField(max_length=50,default=0)

    def register(self):
        self.save()

    def isExist(self):
        if(Customer.objects.filter(Email=self.Email)):
            return True
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(Email=email)
        except:
            return False
            

        