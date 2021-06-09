from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
     
    path('statistics/', views.statistics, name="statistics"), 
    path('customer/<slug:slug>/',views.customer,name='customer'),
    path('productAdmin/',views.productAdminPage,name='productAdmin'),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('upDataProduct/', views.upDataProduct, name="upDataProduct"),
    path('giftVoucher/', views.giftVoucher, name="giftVoucher"),
    path('addBlog/', views.addBlog, name="addBlog"),
    path('chat/', views.chat, name="chat"),
    path('statistics/char/', views.char, name="char"),
    path('productAdminDetail/<slug:slug>/',views.productAdminDetail,name='productAdminDetail'),
    path('customer/',views.listCustomer,name='listCustomer'),
    path('statistics/char/customer', views.charCustomer, name="charCustomer"),

]