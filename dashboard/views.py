from django.shortcuts import render
from .models import *

from ecom.models import *
from chat.models import *
import datetime
from .decorators import admin_only
from .form import addProductForm,updataProductForm


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
@admin_only
def customer(request,pk):
    customer = Customer.objects.get(id = pk)
    order = DataOrder.objects.get(customer = customer)
    total = order.get_total_item
    
    #list product bought
    item = Data.objects.filter(dataOrder= order,complete=True)
    #--------------------------


    #amount login and time used 
    login = LoginAttempts.objects.filter(customer = customer)
    times = login.count()
    date_and_time = datetime.datetime(1, 1, 1, 0, 0, 0)
    for i in login:
        t =  i.end -i.start 
        if  t.days== -1:
            i.delete()
        date_and_time = date_and_time +t
    total_time = str(date_and_time.hour)+"h:"+str(date_and_time.minute)+"min:"+str(date_and_time.second)+"second"
    averageTime =date_and_time.hour*3600+date_and_time.minute*60+date_and_time.second
    averageTime = averageTime/3
    averageTime = convert(averageTime) 
    print(averageTime)
    #----------------------------


    context = {'averageTime':averageTime,'total_time':total_time,'times':times,'customer':customer,'item':item,'total':total}
    return render(request, 'admin/customer.html', context)

@admin_only
def productAdminPage(request):
    products = Product.objects.all()
    context = {'products':products}
 
    return render(request, 'admin/productAdmin.html', context)
    
@admin_only
def statistics(request):
    #Tong so san pham da ban
    data = Data.objects.all()
    total_sales= 0
    for i in data:
        total_sales += i.quantity
    total_customers = Customer.objects.all().count()
    #---------------------------

    #Doanh thu cua moi san pham
    product = Product.objects.all()
    sell ={}
    for product in product:
        data = Data.objects.filter(product = product)
        total =0.0
         
        for data in data:
            total = total+ data.get_total
        sell.setdefault(product,(total))
       
    print(sell)
    #------------------------

    #doanh thu-von-lai rong
    income = Income.objects.all()
    total_revenue = 0.0
    total_cost =0.0
    total_profit = 0.0
    for i in income:
        total_revenue += float(i.total_revenue)
        total_cost += float(i.total_cost)
    total_profit = i.total_profit()
    #-------------------------

    context = {'sell':sell,'total_sales':total_sales,'total_customers':total_customers,'total_revenue':total_revenue,'total_cost':total_cost,'total_profit':total_profit}
    return render(request,'admin/statistics.html',context)
@admin_only
def addProduct(request):
    form = addProductForm()
    context ={'form':form}
    if request.method == 'POST':     
        form = addProductForm(request.POST)  
        
        if form.is_valid():
            Product = form.save()
           
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
    return render(request,'admin/addProduct.html',context)

@admin_only
def upDataProduct(request):
    form1 = updataProductForm()
    print("hello32")  
    context ={'form1':form1}
    if request.method == 'POST':   
        print("hello-")       
        form1 = updataProductForm(request.POST)  
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
            return render(request, 'admin/updataProduct.html',context) 
    return render(request,'admin/updataProduct.html',context)