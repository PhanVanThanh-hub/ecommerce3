import json
from django.shortcuts import render
from .models import *

def cartData(request,pk):
    products = Product.objects.all()
    blogs = Blog.objects.get(id=pk)
    customer = request.user.customer
    item, create = Order.objects.get_or_create(customer=customer)
    favorite1 ,create = Favorite.objects.get_or_create(customer= customer)
    favorite = favorite1.favoriteproduct_set.all()
    order =item.orderitem_set.all()
    for item2 in favorite:
        for item1 in products:
            if item1.name == item2.product.name:
                item1.favorite =1
    sum=0
    for item3 in products:
        if item3.favorite==1:
            sum+=1
    return {'products':products,'order':order,'blogs':blogs,'item':item,'favorite':favorite,'sum':sum}

def ecommerce3Product(request):
    blogs= Blog.objects.all()
    products = Product.objects.all()
    customer = request.user.customer
    item,create= Order.objects.get_or_create(customer=customer)
    favorite1 ,create = Favorite.objects.get_or_create(customer= customer)
    favorite = favorite1.favoriteproduct_set.all()
    order =item.orderitem_set.all()
    for product in products:
        if product.price<=50 and product.price>0:
            product.priceFilter= 50
        if product.price<=100 and product.price>50:
            product.priceFilter = 100
        if product.price<=150 and product.price>100:
            product.priceFilter = 150
        if product.price<=200 and product.price>150:
            product.priceFilter = 200
        if product.price>200:
            product.priceFilter = 300
    for item2 in favorite:
        for item1 in products:
            if item1.name == item2.product.name:
                item1.favorite =1
    sum=0
    for item3 in products:
        if item3.favorite==1:
            sum+=1
    for i in order:
        print("1:",i.quantity)
        if i.quantity == 0:
            i.delete()
    
     
         
    return {'products':products,'order':order,'blogs':blogs,'item':item,'favorite':favorite,'sum':sum}
