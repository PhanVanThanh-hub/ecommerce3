from . import views
from django.urls import path
app_name='Product'
    
urlpatterns = [
    path('productDetail/<slug:slug>/',views.productDetailPage,name='productDetail'),
    path('product/',views.productPage,name='product'),
    path('quickView/',views.quickView,name='quickView'),
]