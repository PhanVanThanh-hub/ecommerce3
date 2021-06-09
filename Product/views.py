from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator
import json
from ecom.models import *

from .decorators import  allowed_users
 
from .utils import ecommerce3Product
from django.contrib.auth import get_user_model
from .form import *
User = get_user_model()
from django.db.models import Q


# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def productDetailPage(request,slug):
     
    product = Product.objects.all()
    products = Product.objects.get(slug=slug)
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
               'room_name_json':mark_safe(json.dumps(products.id)),
               'pic':pic,'countReview':countReview,
               'username':mark_safe(json.dumps(request.user.username))}    
    print("lolo",mark_safe(json.dumps(slug)))
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
    
    # paginator = Paginator(products, 5)
    # page = request.GET.get('page', 1)
    # try:
    #     products_paged = paginator.page(page)
    # except PageNotAnInteger:
    #     products_paged = paginator.page(1)
    # except EmptyPage:
    #     products_paged = paginator.page(paginator.num_pages)
    form = searchProduct()
    context = {'form':form,"products": products,'order':order,'item':item,'favorite':favorite,'sum':sum, 'tag':tag,'type':type}

    
    if request.is_ajax():
        form = searchProduct(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            products=Product.objects.filter(Q(name__icontains=name))
            print("proudcts:",products)
        else : 
            print("hi")
            a=request.POST.get('e')
            print("a:",a)
            if str(a)=="low_to_high":
                products = Product.objects.all().filter().order_by("price")
            elif str(a)=="high_to_low":
                products = Product.objects.all().filter().order_by("-price")
            elif str(a)=="default":
                products = Product.objects.all()
            elif str(a)=="popularity":
                products = Product.objects.all().filter().order_by("-sold")
            elif str(a)=="average_rating":
                products = Product.objects.all().filter().order_by("-rate")
        context = {"products": products,'order':order,'item':item,'favorite':favorite,'sum':sum, 'tag':tag,'type':type}
        return render(request, 'product/productAjax.html', context)
    
    return render(request, 'product/product.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def quickView(request):
    if request.is_ajax():
        id = request.POST.get('productId')
        product= Product.objects.get(id=id)
        context={'product':product}
        print("id:",id)
        return render(request,'product/quickView.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def productSortBy(request,slug):
    data      = ecommerce3Product(request)
    
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
    if slug==low_to_hight:
        products= Product.objects.all().order_by("price")

    context = {"products": products,'order':order,'item':item,'favorite':favorite,'sum':sum, 'tag':tag,'type':type}
    return render(request, 'product/product.html', context)
