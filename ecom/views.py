from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.views.generic import ListView

from django.contrib.auth.hashers import check_password
from django.conf import settings

from datetime import timedelta

from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat.models import *



import re
from dashboard.urls import *
import json
import datetime
from .decorators import unauthenticated_user, allowed_users, admin_only
from .form import customerForm,changePassWordForm
from .utils import cartData,ecommerce3Product
from .filter import productFilter
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
    for i in date:
        a= i.start.strftime('%m/%d/%Y%H%M%S')
        b= i.end.strftime('%m/%d/%Y%H%M%S')

        if (a==b):
            i.delete()
        
        print('sss:',i.start,':',i.end)
    total = 0
    for item in data:
        total += item.product.price * item.quantity
    
    room = Room.objects.all()
    
    context = {'room':room,'customer':customer,'numberUser':numberUser,'data':data,'total':total,'myFilter': myFilter}
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
def blogDetailPage(request,pk):
    data      = cartData(request,pk)
    products  = data['products']
    order     = data['order']
    blogs     = data['blogs']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    context = {'products':products,'order':order,'blogs':blogs,'item':item,'favorite':favorite,'sum':sum}
    
    return render(request, 'pages/blog-detail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def blogPage(request):
    data      = ecommerce3Product(request)
    products  = data['products']
    order     = data['order']
    blogs     = data['blogs']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    context = {'products':products,'order':order,'blogs':blogs,'item':item,'favorite':favorite,'sum':sum}
    return render(request, 'pages/blog.html', context)


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


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def home(request):
    
    print("xL:",request.user.customer.id)
    LoginAttempts.objects.create(
        customer=request.user.customer,
        start=datetime.datetime.now()
    )
    
   
    
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def shopingcartPage(request):
    data      = ecommerce3Product(request)
    products  = data['products']
    order     = data['order']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    print("item:",item.get_total_order)
    context = {'products':products,'order':order,'item':item,'favorite':favorite,'sum':sum}
    return render(request, 'pages/shoping_cart.html', context)

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



@login_required(login_url='login')
def processOrder(request):
    data = json.loads(request.body)
    address = data['shippingInfo']['address']
    state = data['shippingInfo']['state']
    zipcode = data['shippingInfo']['zipcode']
    total = data['total']
    if request.user.is_authenticated:
        customer = request.user.customer
    order= Order.objects.get(customer=customer)
    print("dâta",data)
     
    if order.discount !=1.0:
        discount = Discount.objects.get(customer=customer)
        if discount.amount50 ==0 and discount.amount30 ==0 and discount.amount20 ==0:
            discount.complete=False
        discount.save()
        order.discount=1.0
    print("order:",order)
    print("order:",order.get_total_order)
    print("order1:",order.get_total_item())
    print("total:",total)
    total = order.get_total_item()
    Shiping.objects.create(
        customer =customer,
        order = order,
        address = address,
        state= state,
        zipcode = zipcode
    )

    orderItem = order.orderitem_set.all()
    dataOrder ,create= DataOrder.objects.get_or_create(customer = customer)
    for item in orderItem:
        Data.objects.create(
            dataOrder=dataOrder,
            complete=True,
            quantity=item.quantity,
            product=item.product,
            size = item.size,
            color = item.color,
        ) 
        orderItem.delete()
        print("ok")
    incom=Income.objects.all().latest('id')
    if incom.data_create.month == datetime.datetime.now().month:  
        incom.total_revenue = float(total) +float(incom.total_revenue)
        incom.save()
    else:
        Income.objects.create(
            total_revenue = float(order.get_total_item())
        )  
    order.complete= True
    order.save()
    order.delete()
    return JsonResponse('Payment submitted..', safe=False)

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
 
def discount(request):
    data = json.loads(request.body)
    code = data['discount']
    customer = request.user.customer
    discount = Discount.objects.get(customer=customer)
    order = Order.objects.get(customer=customer)
    print("discount50:",discount.discount50)
    if discount.complete == True:
        if code == discount.discount50 and discount.amount50!=0:
            print("Bigo50")
            order.discount = float(order.discount)-float(order.discount)*0.5
            discount.amount50 -=1
        if code == discount.discount30 and discount.amount50!=0:
            print("Bigo30")
            order.discount = float(order.discount)-float(order.discount)*0.3
            discount.amount30 -=1
        if code == discount.discount20 and discount.amount50!=0:
            print("Bigo20")
            order.discount = float(order.discount)-float(order.discount)*0.2
            discount.amount20 -=1
        discount.save()
    print("order.discount:",order.discount)
    print("discount50:",discount.amount50) 
    print("discount30:",discount.amount30)
    print("discount20:",discount.amount20)
    order.save()
    return JsonResponse('Item was added', safe=False)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer,TaskOrder,ProductList


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}
	return Response(api_urls)

@api_view(['GET'])
def discountList(request):
    customer = request.user.customer
    tasks = Discount.objects.all().filter(customer= customer)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

 

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

 
 