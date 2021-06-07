from django.urls import path

from . import views
app_name='blog'
urlpatterns =[
    path('blogCategory/<slug:slug>/',views.blogCategory,name='category'),
    path('blog/<slug:slug>/',views.blogDetailPage,name='blog_detail'),
    path('blog/', views.blogPage, name='blog'),
]