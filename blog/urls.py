from django.urls import path

from . import views
app_name='blog'
urlpatterns =[
    path('blog-detail/<str:pk>/',views.blogDetailPage,name='blog-detail'),
    path('blog/', views.blogPage, name='blog'),
]