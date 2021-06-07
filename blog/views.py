from django.shortcuts import render 
from .models import *
 
from django.contrib.auth.decorators import login_required
 
from django.core.paginator import Paginator

 
from .decorators import  allowed_users
from .utils import cartData,ecommerce3Product
 
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def blogDetailPage(request,slug):
    data      = cartData(request,slug)
    category = Category.objects.all()
    products  = data['products']
    order     = data['order']
    blogs     = data['blogs']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    context = {'category':category,'products':products,'order':order,'blogs':blogs,'item':item,'favorite':favorite,'sum':sum}
    
    return render(request, 'blog/blog-detail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def blogPage(request):
    category = Category.objects.all()
    data      = ecommerce3Product(request)
    products  = data['products']
    order     = data['order']
    blogs     = data['blogs']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page', 1)
    try:
        blog_paged = paginator.page(page)
    except PageNotAnInteger:
        blog_paged = paginator.page(1)
    except EmptyPage:
        blog_paged = paginator.page(paginator.num_pages)
    context = {'products':products,'order':order,'blogs':blog_paged,'item':item,'favorite':favorite,'sum':sum,'category':category}
    return render(request, 'blog/blog.html', context)

def blogCategory(request,slug):
    category = Category.objects.all()
    data      = ecommerce3Product(request)
    products  = data['products']
    order     = data['order']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    print("slugP:",slug)
    categorys=Category.objects.get(slug= slug)
    print("ca:",categorys)
    blogs=Blog.objects.all().filter(category=categorys)
    print("ca:",blogs)
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page', 1)
    try:
        blog_paged = paginator.page(page)
    except PageNotAnInteger:
        blog_paged = paginator.page(1)
    except EmptyPage:
        blog_paged = paginator.page(paginator.num_pages)
    context = {'blogs':blog_paged,'order':order,'item':item,'favorite':favorite,'sum':sum,'category':category}

    return render(request, 'blog/blog.html', context)

