import json
from django.shortcuts import render
from ecom.models import *
def ecommerce3Product(request):
    customer = request.user.customer
    item,create= Order.objects.get_or_create(customer=customer)
    favorite1 ,create = Favorite.objects.get_or_create(customer= customer)
    favorite = favorite1.favoriteproduct_set.all()
    order =item.orderitem_set.all()
    for i in order:
        print("1:",i.quantity)
        if i.quantity == 0:
            i.delete()
    
     
         
    return {'order':order,'item':item,'favorite':favorite,'sum':sum}

# def conversionFormula(request):
#     customer = request.user.customer
#     accumulation =  accumulationCard.objects.get(customer = customer)
