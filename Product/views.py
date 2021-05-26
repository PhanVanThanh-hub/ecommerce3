from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator
import json
from ecom.models import *

from .decorators import  allowed_users
 
from .utils import ecommerce3Product
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def productDetailPage(request,slug):
     
    product = Product.objects.all()
    products = Product.objects.get(id=slug)
    data      = ecommerce3Product(request)
    order     = data['order']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
    author = User.objects.filter(username =request.user.username )[0]
    author_user = Customer.objects.get(user = author)
    pic = author_user.profile_pic.url
    author_user = author_user.name
    
    print("user:",author_user,':',pic)      
    comment = Comment.objects.all().filter(product= products).order_by('-data_create') 
    countReview =Comment.objects.all().filter(product= products).count
    paginator = Paginator(comment, 3)
    page = request.GET.get('page', 1)
    try:
        comment_paged = paginator.page(page)
    except PageNotAnInteger:
        comment_paged = paginator.page(1)
    except EmptyPage:
        comment_paged = paginator.page(paginator.num_pages)
    context = {'product':product,'products':products,
               'item':item,'order':order,'favorite':favorite,'sum':sum,
               'comment':comment_paged,
               'author_user':mark_safe(json.dumps(author_user)),
               'room_name_json':mark_safe(json.dumps(slug)),
               'pic':pic,'countReview':countReview,
               'username':mark_safe(json.dumps(request.user.username))}    
    print("lolo")
    return render(request, 'product/product_detail.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def productPage(request):     
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
    paginator = Paginator(products, 5)
    page = request.GET.get('page', 1)
    try:
        products_paged = paginator.page(page)
    except PageNotAnInteger:
        products_paged = paginator.page(1)
    except EmptyPage:
        products_paged = paginator.page(paginator.num_pages)
    print("productL:",products)
    context = {"products": products_paged,'order':order,'item':item,'favorite':favorite,'sum':sum, 'tag':tag,'type':type}
    return render(request, 'product/product.html', context)
