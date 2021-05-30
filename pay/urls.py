from django.urls import path

from . import views
app_name='pay'
urlpatterns =[
    path('shopingCart/',views.shopingcartPage,name='shopingCart'),
    path('discount/', views.discount, name="discount"),
    path('process_order/', views.processOrder, name="processOrder"),
    path('exchange/', views.exchange, name="exchange"),
  
]