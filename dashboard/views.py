from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from ecom.models import *
from pay.models import *
from chat.models import *
import datetime
from .decorators import admin_only
from .form import AddProductForm, GiftVoucherForm,UpdataProductForm,AddBlogForm


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
@admin_only
def customer(request,slug):
 
    #------------------------
    customer = Customer.objects.get(slug = slug)
    
     
    
    #list product bought
    try:
        order = DataOrder.objects.get(customer = customer)
        total = order.get_total_item
        item = Data.objects.filter(dataOrder= order,complete=True).order_by("-date_complete")
    except:
        total=0
        item=[]
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
    averageTime = averageTime/times
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
    #--------------------------
    #Tong so khach hang
    total_customers = Customer.objects.all().count()
    #---------------------------

    


    #Ty le tang truong moi thang:
    tyle = Income.objects.all().order_by("-data_create")[:2]
   
    revenue=[]
    for i in tyle:
        revenue.append(float(i.total_revenue))
    growl=Income.objects.all().latest('id')
    per= revenue[1]/100
    if revenue[1] >revenue[0]:
        growl.growth_revenue=-round(100.0 -revenue[0]/per, 2) 
    else:
        growl.growth_revenue=round(revenue[0]/per-100.0, 2)
    
    profit=[]
    for i in tyle:
        profit.append(float(i.total_profit()))
    per= profit[1]/100
    if profit[1] >profit[0]:
        growl.growth_profit=-round(100.0 -profit[0]/per, 2) 
    else:
        growl.growth_profit=round(profit[0]/per-100.0, 2)

    print("12:",growl.growth_profit,':',growl.growth_revenue)
    growl.save()
    #---------------------------
    #doanh thu-von-lai rong
    income = Income.objects.all()
    total_revenue = 0.0
    total_cost =0.0
    total_profit = 0.0
    for i in income: 
        total_revenue += float(i.total_revenue)
        total_cost += float(i.total_cost)
        total_profit += float(i.total_profit())

    for i in income:
        i.growth_total_revenue=round(float(i.total_revenue) /float(total_revenue/100),2) 
        i.growth_total_cost=round(float(i.total_cost) /float(total_cost/100),2) 
        i.growth_total_profit=round(float(i.total_profit()) /float(total_profit/100),2) 
        i.save()
     
    income = Income.objects.all()
    #-------------------------
    #--------------------------
    

    #--------------------------
    #Bill
    bill = Bill.objects.all()
    #____________________________
    context = {'income':income,'total_sales':total_sales,'total_customers':total_customers,'total_revenue':total_revenue,'total_cost':total_cost,'total_profit':total_profit}
    return render(request,'admin/statistics.html',context)
@admin_only
def addProduct(request):
    form = AddProductForm()
    context ={'form':form}
    if request.is_ajax():    
        form = AddProductForm(request.POST)  
        if form.is_valid():
            Product = form.save()
            if 'images1' in request.FILES:
                Product.images1 = request.FILES['images1']
            if 'images2' in request.FILES:
                Product.images2 = request.FILES['images2']
            if 'images3' in request.FILES:
                Product.images3 = request.FILES['images3']
            Product.save()
           
            context ={'products':Product}
            print("dmm")

            #Tinh bill
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
            #---------------------------------------------
            return render(request, 'product/productPreview.html',context)
    return render(request,'admin/addProduct.html',context)

@admin_only
def upDataProduct(request):
    form1 = UpdataProductForm()
    print("hello32")  
    context ={'form1':form1}
    if request.method == 'POST':   
        print("hello-")       
        form1 = UpdataProductForm(request.POST)  
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

@admin_only
def giftVoucher(request):
    form = GiftVoucherForm()
    context ={'form':form}
    if request.method == 'POST':   
        print("hello-")       
        form = GiftVoucherForm(request.POST)  
        print("form:",form.is_valid())
        if form.is_valid():
            giftVoucher = form.save()
            
        return render(request, 'admin/gift.html',context)
    print("fomr:",form)
    return render(request,'admin/gift.html',context)

@admin_only
def addBlog(request):
    form = AddBlogForm()
    context ={'form':form}
    if request.is_ajax():
        print("ok")
        fromProduct = AddBlogForm(request.POST)
        if fromProduct.is_valid():
            a= fromProduct.cleaned_data.get('name')
            Blog = fromProduct.save()
            if 'images1' in request.FILES:
                Blog.images1 = request.FILES['images1']
            Blog.save()
             
             
            print("blog:",Blog.detail)
            context ={'blogs':Blog}
            print("222")
            return render(request, 'blog/blogDetail.html', context)

    return render(request,'admin/addBlog.html',context)

@admin_only
def chat(request):
    author = request.user.username
    print("author:L",type(author))
    # roomName = slug
    # id =User.objects.get(username =roomName )
    # room =Room.objects.get(nameRoom = id)
    # messages = Message.last_10_messages(room)
    # for mesage in messages:
    #     print("s:",str(mesage))
    #     if str(mesage) == "admin":
    #         print("1:",mesage.author)
    #     else:
    #         print("ngu")
    #admin hay not
    a = str(author)
    b=Room.objects.all().order_by('-timestamp') 
    #---------------------
    context = { 'b':b ,
                # 'room_name_json':mark_safe(json.dumps(slug)),
                # 'username':mark_safe(json.dumps(request.user.username))
                }
    if request.is_ajax():
        print("hpla")
    return render(request, 'chat/chat2.html',context)


@admin_only
def char(request):
    #Doanh thu cua moi san pham
    product = Product.objects.all()
    sell ={}
    for product in product:
        data = Data.objects.filter(product = product)
        total =0.0
         
        for data in data:
            total = total+ data.get_total
        sell.setdefault(product,(total))
    #--------------------------------

    #Doanh thu moi thang
    income = Income.objects.all()
    context={"sell":sell,'income':income}
    #------------------------

    #Top khach hang
    top={}
    customer = Customer.objects.all()
    for i in customer:
        try:  
            order = DataOrder.objects.get(customer = i)
            total = order.get_total_item()
            top.setdefault(i,(total))
        except:
            print("oh no!")
         
    
    top= sorted(top.items(), key=lambda x: x[1], reverse=True)
    top = top[:10]
    #-------------------------------------------
    

    #So luong san pham ban ra
    amount = {}
    product = Product.objects.all()
    for i in product:
        data= Data.objects.all().filter(product = i)
        t=0
        for x in data:
           t= t+int(x.quantity)
        amount.setdefault(i,(t))
    amount= sorted(amount.items(), key=lambda x: x[1], reverse=True)
    amount = amount[:10]

    #------------------------------------------

    #Khu vuc mua hang
    shiping =Shiping.objects.all()
    country1= country.objects.all()
    address={}
    for i in country1:
        if Shiping.objects.all().filter(address=i.name).count()!=0:
            address.setdefault(i,int(Shiping.objects.all().filter(address=i.name).count()))
    address= sorted(address.items(), key=lambda x: x[1], reverse=True)
    address = address[:10]
    #------------------------------------------
    context={"sell":sell,'income':income,'top':top,'amount':amount,'address':address,}
    return render(request, 'char/char.html',context)

def productAdminDetail(request,slug):
 
    #------------------------
    products = Product.objects.get(slug = slug)
    print("clgt?")
    context={"products":products}
    return render(request,'product/ProductPreview.html',context)

@admin_only
def listCustomer(request):
    customer = Customer.objects.all()
    context={'customer':customer}
    
    
    return render(request,"admin/listCustomer.html",context)

@admin_only
def charCustomer(request):
    print("hi Phan Van Thanh")
    context={}
    return render(request, 'char/charCustomer.html',context)