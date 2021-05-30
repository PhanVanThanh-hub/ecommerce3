from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.views.generic import ListView
from django.conf import settings

from datetime import timedelta

from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat.models import *
from dashboard.models import *


import re
from dashboard.urls import *
import json
import datetime
from .decorators import unauthenticated_user, allowed_users, admin_only
from .form import customerForm,changePassWordForm
from .utils import cartData,ecommerce3Product
from .filter import productFilter
from pay.models import *
# Create your views here.
@login_required(login_url='login')
@admin_only
def dashboardPage(request):
    customer = Customer.objects.all()
    numberUser = customer.count()
    data = Data.objects.all().filter(complete=True)
    myFilter = productFilter(request.GET,queryset=data)
    data = myFilter.qs
    date = LoginAttempts.objects.all() 
    total = 0
    for item in data:
        total += item.product.price * item.quantity
    
    room = Room.objects.all()
    paginator = Paginator(data, 10)
    page = request.GET.get('page', 1)
    try:
        products_paged = paginator.page(page)
    except PageNotAnInteger:
        products_paged = paginator.page(1)
    except EmptyPage:
        products_paged = paginator.page(paginator.num_pages)
     
    context = {'data':products_paged,'room':room,'customer':customer,'numberUser':numberUser,'total':total,'myFilter': myFilter}
    return render(request, 'admin/dashboard.html', context)
 
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def changePassWord(request):
    form = changePassWordForm()
    customer1 = request.user.customer
    customer = request.user
     
    if request.method == 'POST':
        form = changePassWordForm(request.POST)     
        if form.is_valid():
            currentPassword = form.cleaned_data.get('currentPassword')
            newPassword = form.cleaned_data.get('newPassword')
            confirmPassword=form.cleaned_data.get('confirmPassword')
            print("username",currentPassword)
            if customer.check_password(currentPassword):
                while True:  
                    if (len(newPassword)<8):
                        flag = -1
                        break
                    elif not re.search("[a-z]", newPassword):
                        flag = -1
                        break
                    elif not re.search("[A-Z]", newPassword):
                        flag = -1
                        break
                    elif not re.search("[0-9]", newPassword):
                        flag = -1
                        break
                    else:
                        flag = 0
                        print("Valid Password")
                        break 
                if flag ==0:
                    if  newPassword == confirmPassword:
                        print("customer1:",customer1)
                        old = oldPassWord.objects.all().filter(customer= customer1)
                        print("old:",old)
                        for password in old:
                            print("old1:",password.oldPassWord)
                            if password.oldPassWord == newPassword:
                                flag=2
                                messages.info(request, 'Is the same as the old password')
                                break
                        if flag !=2:
                            oldPassWord.objects.create(
                                customer=customer1,
                                oldPassWord= currentPassword
                            )
                            customer.set_password(newPassword)
                            customer.save()
                            messages.info(request, 'Updated Password')
                            return redirect('login')
                else:
                    messages.info(request, 'Invalid password')
            else:
                messages.info(request, 'wrong password')
    print("user:")
    print("user1:",request.user.password)
    context = {'form': form}
    return render(request,'pages/changePassWord.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def aboutPage(request):
    products = Product.objects.all()
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
    context = {'products':products,'order':order,'item':item,'favorite':favorite,'sum':sum}
    return render(request, 'pages/about.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def contactPage(request):
    data      = ecommerce3Product(request)
    products  = data['products']
    order     = data['order']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    context = {'products':products,'order':order,'item':item,'favorite':favorite,'sum':sum}
    return render(request, 'pages/contact.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def home2Page(request):
    data      = ecommerce3Product(request)
    products  = data['products']
    products  = data['products']
    order     = data['order']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    context = {'products':products,'order':order,'item':item,'favorite':favorite,'sum':sum}
    return render(request, 'pages/home2.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def home3Page(request):
    data      = ecommerce3Product(request)
    products  = data['products']
    order     = data['order']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    context = {'products':products,'order':order,'item':item,'favorite':favorite,'sum':sum}
    return render(request, 'pages/home3.html', context)

from datetime import timedelta 
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def home(request):
    
    print("xL:",request.user.customer.id)
    LoginAttempts.objects.create(
        customer=request.user.customer,
        start=datetime.datetime.now()
    )
    #Tang gift voucher
    gift = giftVoucher.objects.all()[0]
    a=((gift.dateTimeGift).strftime("%Y%b%d"))
    b=((datetime.datetime.now()).strftime("%Y%b%d"))
    print(a)
    if str(a) == str(b):
        x = LoginAttempts.objects.all().filter(start>=gift.dateTimeGift).count()
        if x==1:
            customer = Customer.objects.get(user = request.user)
            discount = Discount.objects.get(customer= customer)
            discount.amount50 = int(discount.amount50)+ int(gift.amount50)
            discount.amount30 = int(discount.amount30)+ int(gift.amount30)
            discount.amount20 = int(discount.amount20)+ int(gift.amount20)
            discount.complete = True
            discount.save()
    if gift.dateTimeGift<datetime.datetime.now():
        gift.delete()
    #-----------------------------


    
    
    
    data      = ecommerce3Product(request)
    products  = data['products']
    order     = data['order']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    sum1 = len(Product.TAGS)
    
    tag ={}
    for i in range(sum1):
        tag[i]= Product.TAGS[i][1]
    type ={}
    sum2 = len(Product.TYPE)
    for i in range(sum2):
        type[i]= Product.TYPE[i][1]
    print("sum2:",tag)

    if request.is_ajax():
        print('dmm')
        productId=request.POST.get('productId')
        product = Product.objects.filter(id = productId)
        product = serializers.serialize('json', product)
        return JsonResponse({'product':product },safe=False)

    context = { 'products':products,'order':order,'item':item,'favorite':favorite,'sum':sum,'tag':tag,'type':type}
    return render(request, 'pages/index.html', context)


 

from django.forms.models import model_to_dict
from django.core import serializers
def addCartItem(request):
    if request.is_ajax():
        productId=request.POST.get('productId')
        action=request.POST.get('action')
        customer = request.user.customer
        product = Product.objects.get(id=productId)
         
        size=request.POST.get('size')
        color=request.POST.get('color')
        print("actin:",action)
        order, created = Order.objects.get_or_create(customer=customer)
        total = order.get_total_item()
        quantity = order.get_total_order()
        change=1
        if product.amout ==0 :
            change = 0
        if action == "create":
            value=int(request.POST.get('value'))
             
            product.amout = float(product.amout)-float(value)
            product.save()
            try:
                OrderItems = OrderItem.objects.get(order=order,product=product,size = size , color = color)
            except OrderItem.DoesNotExist:
                OrderItems = None
            if OrderItems is None:
                OrderItems =OrderItem.objects.create(
                    order=order,
                    product = product,
                    quantity=value,
                    size =size,
                    color =color
                )
                OrderItems.save()
            else:
                OrderItems.quantity =OrderItems.quantity + value
                OrderItems.save()
            orderItem = OrderItem.objects.filter(order = order)
            quantity = quantity +value
            
        else :
            
            if size=="M":
                size == "Size M"
            elif size=="L":
                size == "Size L"
            elif size=="S":
                size == "Size S"
            elif size=="XL":
                size == "Size XL"   
            
            orderItem = OrderItem.objects.get(order = order , product = productId,size = size,color=color)
             
            print("total:",total)
            if action == "add":
                orderItem.quantity = orderItem.quantity +1
                product.amout = float(product.amout)-1
                product.save()
                total = total + orderItem.product.price
                quantity = quantity +1
                orderItem.save()
               
            elif action =="remove":
                orderItem.quantity = orderItem.quantity -1
                quantity = quantity -1
                product.amout = float(product.amout)+1
                total = total - orderItem.product.price
                product.save()
                orderItem.save()
                
            if orderItem.quantity ==0:
                product.amout=0
                product.save()
                orderItem.delete()
                print("delete")
        order = order.orderitem_set.all()
        order = serializers.serialize('json', order)
    return JsonResponse({'quantity':quantity,'total':total,'change':change },safe=False)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettingPage(request):
    customer =request.user.customer
    item, create = Order.objects.get_or_create(customer=customer)
    order =item.orderitem_set.all()
    form =customerForm(instance =customer)
    if request.method == 'POST':
        form = customerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form,'order':order,'item':item}
    return render(request,'pages/accounts_setting.html',context)



 

def addFavorite(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = 1
    try:
        action = data['action']
    except:
        print("An exception occurred")
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    favorite ,created =Favorite.objects.get_or_create(customer=customer)
    favoriteProduct, created = FavoriteProduct.objects.get_or_create(product=product,favorite=favorite)
    print("product:",action)
    if action == 'remove' :
        favoriteProduct.delete()
    return JsonResponse('Item was added', safe=False)
 
 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskOrder,ProductList


 


 

@api_view(['GET'])
def orderList(request):
    customer = request.user.customer
    item = Order.objects.get(customer= customer)
    order=item.orderitem_set.all()
    serializer = TaskOrder(order, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productList(request):
    product = Product.objects.all()
    serializer = ProductList(product, many=True)
    return Response(serializer.data)

def totalItemList(request):
    customer = request.user.customer
    item = Order.objects.get(customer= customer)
    order=item.orderitem_set.all()
    context={}
    for i in order:
        print("i:",i.quantity)
    context={'order':order}
    return JsonResponse(context)

def list(request):
	return render(request, 'pages/listProductAdmin.html')

 
 