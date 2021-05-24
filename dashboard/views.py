from django.shortcuts import render
from .models import *

from ecom.models import *
from chat.models import *
import datetime
from .decorators import admin_only
from .form import addProductForm,updataProductForm
 
@admin_only
def customer(request,pk):
    customer = Customer.objects.get(id = pk)
    order = DataOrder.objects.get(customer = customer)
    total = order.get_total_item
    item = Data.objects.all().filter(dataOrder= order,complete=True)
     
    context = {'customer':customer,'item':item,'total':total}
 
    return render(request, 'admin/customer.html', context)

@admin_only
def productAdminPage(request):
    products = Product.objects.all()
    context = {'products':products}
 
    return render(request, 'admin/productAdmin.html', context)
    
@admin_only
def statistics(request):
    data = Data.objects.all()
    total_sales= 0
    for i in data:
        total_sales += i.quantity
    total_customers = Customer.objects.all().count()

    income = Income.objects.all()
    total_revenue = 0.0
    total_cost =0.0
    total_profit = 0.0
    for i in income:
        total_revenue += float(i.total_revenue)
        total_cost += float(i.total_cost)
    total_profit = i.total_profit()
    print('toatl:',total_revenue,':',total_cost,':',total_profit)
    context = {'total_sales':total_sales,'total_customers':total_customers,'total_revenue':total_revenue,'total_cost':total_cost,'total_profit':total_profit}
    return render(request,'admin/statistics.html',context)
@admin_only
def addProduct(request):
    form = addProductForm()
    form1 = updataProductForm()
    print("hello32")  
    context ={'form':form,'form1':form1}
    if request.method == 'POST':   
        print("hello-")       
        form1 = updataProductForm(request.POST, prefix='banned')  
        print("form1:",form1.is_valid())
        if form1.is_valid():    
            print("hello")     
            name = form1.cleaned_data.get('name')
            price = form1.cleaned_data.get('price')
            amount = form1.cleaned_data.get('amout')
            cost = form1.cleaned_data.get('cost')
            customer1 = Customer.objects.all()
             
            name.price = price
            name.amout = name.amout + amount
            name.cost = cost
            name.save()
            Bill.objects.create(
                product = name,
                amount= amount,
                cost= cost
            )
            incom=Income.objects.all().latest('id')
            if incom.data_create.month == datetime.datetime.now().month:
                print("xxxxxxxxxxx")
                incom.total_cost = float(name.cost) * float(amount)+ float(incom.total_cost)
                incom.save()
            else:
                Income.objects.create(
                    total_cost= float(name.cost) * float(amount)
                )  
            return render(request, 'admin/addProduct.html',context) 
    else:
        print("111111111")
        form1 =updataProductForm(prefix='banned')

    if request.method == 'POST' and not form1.is_valid(): 
        print("hello1*")     
        form = addProductForm(request.POST, prefix='expected')   
        form1 =updataProductForm(prefix='banned')
        print("form1:",form1.is_valid())
        print("form:",form.is_valid())
        if form.is_valid():
            print("hello1") 
            Product = form.save()
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            amount = form.cleaned_data.get('amout')
            cost = form.cleaned_data.get('cost')
            
            Bill.objects.create(
                product = Product,
                amount= amount,
                cost= cost
            )
            incom=Income.objects.all().latest('id')
            if incom.data_create.month == datetime.datetime.now().month:
                incom.total_cost = float(cost) * float(amount)+ float(incom.total_cost)
                incom.save()
            else:
                Income.objects.create(
                    total_cost= float(product.cost) * float(amount)
                )  
            return render(request, 'admin/addProduct.html',context)
            
    else:
        print("22222")
        form = addProductForm(prefix='expected')

     


    return render(request,'admin/addProduct.html',context)