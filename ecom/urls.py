from django.urls import path

from . import views
 
urlpatterns =[
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('accountSetting/',views.accountSettingPage,name='accountSetting'),
    path('changePassWord/',views.changePassWord,name='changePassWord'),
    path('',views.dashboardPage,name='home'),
    
    path('user/', views.home, name='user-page'),
    path('about/',views.aboutPage,name='about'),
    path('blog-detail/<str:pk>/',views.blogDetailPage,name='blog-detail'),
    path('blog/', views.blogPage, name='blog'),
    path('contact/', views.contactPage, name='contact'),
    path('home2/', views.home2Page, name='home2'),
    path('home3/', views.home3Page, name='home3'),
    path('shopingCart/',views.shopingcartPage,name='shopingCart'),
    path('add_cart_item/', views.addCartItem, name="addCartItem"),
    
    path('discount/', views.discount, name="discount"),
    
    path('add_favorite/', views.addFavorite, name="addFavorite"),
    path('process_order/', views.processOrder, name="processOrder"),

    path('totalItemList/', views.totalItemList, name="totalItemList"),

    path('viewAPI/', views.apiOverview, name="api-overview"),
    path('ordetItemList/', views.orderList, name="orderList"),
    path('productList/', views.productList, name="productList"),
	path('discoutList/', views.discountList, name="discoutList"),
    path('list/', views.list, name="list"),

 
]