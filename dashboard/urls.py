from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
     
    path('statistics/', views.statistics, name="statistics"), 
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('productAdmin/',views.productAdminPage,name='productAdmin'),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('upDataProduct/', views.upDataProduct, name="upDataProduct"),
    path('giftVoucher/', views.giftVoucher, name="giftVoucher"),
]