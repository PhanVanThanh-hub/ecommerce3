from . import views
from django.urls import path
app_name='Product'
    
urlpatterns = [
    path('product/<slug:slug>/',views.productDetailPage,name='product_detail'),
    path('product/',views.productPage,name='product'),
    path('quickView/',views.quickView,name='quickView'),
    path('product/sortBy/<slug:slug>/',views.productSortBy,name='productSortBy'),
   
]