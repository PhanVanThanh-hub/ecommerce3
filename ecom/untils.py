import json
from django.shortcuts import render
from .models import *

def quickView(request):
    data = json.loads(request.body)
    productId = data['productId']
    print("productId:1212",productId)
    products = Product.objects.get(id=productId)
    context = {'products':products}
    return {'productId':productId}
    
    