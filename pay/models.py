from django.db import models
from django.contrib.auth.models import User
from ecom.models import Customer
# Create your models here.
 
class Discount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,related_name="list12",null=True)
    amount50 = models.IntegerField(default=0, null=True, blank=True)
    amount30 = models.IntegerField(default=0, null=True, blank=True)
    amount20 = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.customer.name

class accumulationCard(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    accumulatedPoints =models.DecimalField(max_digits=8,null=True,decimal_places=2)
    data_create = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.customer.name


 