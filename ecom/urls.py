from django.urls import path

from . import views
 
urlpatterns =[
 

    path('accountSetting/',views.accountSettingPage,name='accountSetting'),
    path('changePassWord/',views.changePassWord,name='changePassWord'),
    path('',views.dashboardPage,name='home'),
    
    path('user/', views.home, name='user-page'),
    path('about/',views.aboutPage,name='about'),
    path('contact/', views.contactPage, name='contact'),
    path('home2/', views.home2Page, name='home2'),
    path('home3/', views.home3Page, name='home3'),
    path('add_cart_item/', views.addCartItem, name="addCartItem"),
    
     
    
    path('add_favorite/', views.addFavorite, name="addFavorite"),
     

    path('totalItemList/', views.totalItemList, name="totalItemList"),

    
    path('ordetItemList/', views.orderList, name="orderList"),
    path('productList/', views.productList, name="productList"),

    path('list/', views.list, name="list"),

 
]