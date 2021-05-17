from . import views
from django.urls import path
app_name='Product'

urlpatterns = [
    path('productDetail/<str:pk>/',views.productDetailPage,name='productDetail'),
    path('product/',views.productPage,name='product'),
]