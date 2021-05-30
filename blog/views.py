from django.shortcuts import render 
from .models import *
 
from django.contrib.auth.decorators import login_required
 
from django.core.paginator import Paginator

 
from .decorators import  allowed_users
from .utils import cartData,ecommerce3Product
 
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
    
    return render(request, 'blog/blog-detail.html', context)


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
    for blog in blogs:
        print("1",blog.data_ordered)
    context = {'products':products,'order':order,'blogs':blogs,'item':item,'favorite':favorite,'sum':sum}
    return render(request, 'blog/blog.html', context)
