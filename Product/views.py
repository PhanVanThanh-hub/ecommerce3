from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from ecom.models import *

from .decorators import  allowed_users
from .form import commentForm
from ecom.utils import ecommerce3Product
# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def productDetailPage(request,pk):
    print("hello")
    product = Product.objects.all()
    products = Product.objects.get(id=pk)
    data      = ecommerce3Product(request)
    order     = data['order']
    item      = data['item']
    favorite  = data['favorite']
    sum       = data['sum']
     
    form = commentForm()
    customer = request.user.customer
    comment = Comment.objects.all().filter(product= products).order_by('-data_create') 
    paginator = Paginator(comment, 3)
    page = request.GET.get('page', 1)
    try:
        comment_paged = paginator.page(page)
    except PageNotAnInteger:
        comment_paged = paginator.page(1)
    except EmptyPage:
        comment_paged = paginator.page(paginator.num_pages)
    context = {'product':product,'products':products,'item':item,'order':order,'favorite':favorite,'sum':sum,'form':form,'comment':comment_paged}
    if request.method == 'POST':    
        form = commentForm(request.POST)
        print("5",form.is_valid())     
        if form.is_valid():
            print("6")
            commnet1 = form.cleaned_data.get('comment')
            Comment.objects.create(
                customer= customer,
                product = products,
                comment = commnet1,
                rate = 1.0
            )   
            return render(request, 'product/product_detail.html', context)       
     
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

    context = {"products": products_paged,'order':order,'item':item,'favorite':favorite,'sum':sum, 'tag':tag,'type':type}
    return render(request, 'product/product.html', context)
