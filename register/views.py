from django.shortcuts import render, redirect
from ecom.models import *
 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
 
from .form import CreateUserForm
from pay.models import *
from chat.models import *
from dashboard.models import *
from pay.models import *
from datetime import timedelta
import datetime
from  .decorators import unauthenticated_user
 
# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            print(phone[0])
            if phone.isnumeric() == False or phone[0] != '0':
                messages.success(request, 'Phone illegal')
            else:
                user = form.save()
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                Customer.objects.create(
                    user=user,
                    name = username,
                    email = email,  
                    phone = phone
                )

                #Tao room
                room = Room.objects.create(nameRoom = user)
                Message.objects.create(room = room,author =user)
                 
                #-----------------
                 
                #Tao password cu
                customer1 = Customer.objects.get(user = user)
                oldPassWord.objects.create(
                    customer = customer1
                )
                #------------------
                
                #Tao ma giam gia
                Discount.objects.create(customer = customer1)
                #-----------------------

                #Tao tai khoan tich luy
                customer = Customer.objects.get(user = user)
                accumulationCard.objects.create(customer=customer)
                #---------------
                messages.success(request, 'Account was creted for ' + username)
                return redirect('login')
    context = {'form': form}
    return render(request, 'register/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("password:",password)
        user = authenticate(request, username=username, password=password)
        print('user:',user)
        if user is not None: 
            login(request, user)
            if(username !="admin"):
                LoginAttempts.objects.create(
                    customer=request.user.customer,
                    start=datetime.datetime.now()
                )
             
                #Tang gift voucher
                countGift = giftVoucher.objects.all().filter(complete=False).count()#check so luong gift
                print("a",countGift)
                if countGift !=0:
                    gift = giftVoucher.objects.all()[0]
                    c= gift.dateTimeGift+datetime.timedelta(days=1)
                    if c<datetime.datetime.now():#xoa gift da het han
                        gift.complete=True
                        gift.save()
                        
                countGift1 = giftVoucher.objects.all().filter(complete=False).count()#check so luong gift sau khi xoa gift da het han
                gift = giftVoucher.objects.all().filter(complete=False)[0]#lay gift dau tien
                if countGift1!=0:#check xem co ton tai gift con time khong
                    a=((gift.dateTimeGift).strftime("%Y%b%d"))
                    b=((datetime.datetime.now()).strftime("%Y%b%d"))
                    if str(a) == str(b):
                        c=0
                        x = LoginAttempts.objects.all().filter(customer=request.user.customer)
                        for i in x:
                            if  i.start>=gift.dateTimeGift:
                                c=c+1
                        if c==1:
                            discount = Discount.objects.get(customer= request.user.customer)
                            discount.amount50 = int(discount.amount50)+ int(gift.amout50)
                            discount.amount30 = int(discount.amount30)+ int(gift.amout50)
                            discount.amount20 = int(discount.amount20)+ int(gift.amout50)
                            discount.complete = True
                            discount.save()
                #-----------------------------
            return redirect('home')  
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'register/login.html', context)

def logoutUser(request):
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
        if group != 'admin':
            t=LoginAttempts.objects.filter(customer=request.user.customer).latest('th')
            t.end = datetime.datetime.now()
            t.save()
            print('tL',t.start,':',t.customer,':',t.end,':',t.th)
    
            t.save()
        
    logout(request)
    return redirect('login')
