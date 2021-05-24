from django.shortcuts import render, redirect
from ecom.models import *
 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
 
from django.contrib.auth.models import Group, 

 
from django.conf import settings
 
from ecom.form import CreateUserForm

from dashboard.urls import *
 
import datetime
from ecom.decorators import unauthenticated_user, 
 
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
                customer1 = Customer.objects.get(user = user)
                oldPassWord.objects.create(
                    customer = customer1
                )
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
