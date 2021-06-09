from django.shortcuts import render
from ecom.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
import datetime


from .decorators import  allowed_users
from .utils import ecommerce3Product
from .models import *

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def shopingcartPage(request):
    data      = ecommerce3Product(request)
    
    order     = data['order']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']

    #create discount:
    user = request.user
    customer = Customer.objects.get(user = user)
    print("1",type(customer))
    
    discount = Discount.objects.get(customer= customer)
    customer = request.user.customer
    accumulation = accumulationCard.objects.get(customer = customer)
    context = { 'discount':discount,'accumulation':accumulation,
                'order':order,'item':item,
                'favorite':favorite,'sum':sum}
    return render(request, 'pay/shoping_cart.html', context)



import datetime
@login_required(login_url='login')
def processOrder(request):
    data = json.loads(request.body)
    address = data['shippingInfo']['address']
    state1 = data['shippingInfo']['state']
    zipcode = data['shippingInfo']['zipcode']
    total = data['total']
    if request.user.is_authenticated:
        customer = request.user.customer
    order= Order.objects.get(customer=customer)
    total = order.get_total_item()
    print("Taotal,",total)
    c =country.objects.get(name=address)
    state.objects.get_or_create(country=c,
                                name=state1
    )
    
    dataOrder ,create= DataOrder.objects.get_or_create(customer = customer)
    Shiping.objects.create(
        customer =customer,
        data = dataOrder,
        address = address,
        state= state1,
        zipcode = zipcode
    )

    #Them du lieu  mua hang
    orderItem = order.orderitem_set.all()
    dataDiscount = 0
    if order.discount !=1:
        dataDiscount =float(1)-float(order.discount)
     
    for item in orderItem:
        Data.objects.create(
            dataOrder=dataOrder,
            complete=True,
            quantity=item.quantity,
            product=item.product,
            size = item.size,
            color = item.color,
            discount= dataDiscount
        ) 
        product = Product.objects.get(name=item.product)
        product.sold= product.sold + int(item.quantity)
        product.save()
        print("itemProduct:",item.product,'|str:',str(item.product))
        orderItem.delete()
        print("ok")
    #---------------------------------
    #Tinh diem tich luy
    customer = request.user.customer
    accumulation = accumulationCard.objects.get(customer = customer)
    accumulation.accumulatedPoints =int(accumulation.accumulatedPoints) + int(total/2)
    print("hey:",accumulation.accumulatedPoints)
    accumulation.save()
     
    #---------------------------------
    #Tinh doanh thu
    incom=Income.objects.all().latest('id')
    if incom.data_create.month !=datetime.datetime.now().month:
        Income.objects.create(
            total_revenue=0,
            total_cost=0
        )
        incom=Income.objects.all().latest('id')
    if incom.data_create.month == datetime.datetime.now().month:  
        incom.total_revenue = float(total) +float(incom.total_revenue)
        incom.save()
    else:
        Income.objects.create(
            total_revenue = float(order.get_total_item())
        ) 
    #---------------------------------- 
    if order.discount !=1.0:
        order.discount=1.0
    order.complete= True
    order.save()
    order.delete()
    return JsonResponse('Payment submitted..',safe=False)



from django.http import JsonResponse
def discount(request):
    if request.is_ajax():
        code = int(request.POST.get('discount'))
        customer = request.user.customer
        discount = Discount.objects.get(customer=customer)
        order = Order.objects.get(customer=customer)
        if discount.complete == True:
            if code == 50 :
                order.discount = float(order.discount)-float(order.discount)*0.5
                discount.amount50 -=1
            if code == 30:
                order.discount = float(order.discount)-float(order.discount)*0.3
                discount.amount30 -=1
            if code == 20:
                order.discount = float(order.discount)-float(order.discount)*0.2
                discount.amount20 -=1
            if discount.amount50==0 and discount.amount30==0 and discount.amount20==0:
                discount.complete=False
            discount.save()
        order.save()
        
        #Tinh total
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
        total = order.get_total_item()
        #---------------------------------------------
        return JsonResponse({'total':total},safe=False)

 
 
def exchange(request):
    if request.is_ajax():
        code = request.POST.get('discount')
        Customer = request.user.customer
        accumulation = accumulationCard.objects.get(customer = Customer)
        discount= Discount.objects.get(customer = Customer)
        point =float(accumulation.accumulatedPoints)
        value = 1
        print("poi:",point,':',type(point),'type:',type(800.0))
        if point >= 1000.0:
            print("ngu")
        if code == "accumulation50" and point>=1500.0 :
            accumulation.accumulatedPoints = float(accumulation.accumulatedPoints)-float(1500)
            discount.amount50 += 1 
            discount.complete = True
            print("50")
        elif code == "accumulation30" and point>=800.0:
            accumulation.accumulatedPoints = float(accumulation.accumulatedPoints)-float(800)
            discount.amount30 += 1 
            discount.complete = True
            print("30")
        elif code == "accumulation20" and point>=500.0:
            accumulation.accumulatedPoints = float(accumulation.accumulatedPoints)-float(500)
            discount.amount20 += 1 
            discount.complete = True
            print("20",accumulation)
        else :
            value=0 
        discount.save()
        point =float(accumulation.accumulatedPoints)
        accumulation.save()
        return JsonResponse({'code':value,'point':point},safe=False)

 









