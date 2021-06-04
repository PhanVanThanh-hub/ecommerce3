# chat/urls.py
from django.urls import path

from . import views
app_name='chat'
urlpatterns = [
    path('chat/<slug:slug>/', views.room, name='chat'),
    path('listAjax/',views.listAjax, name='chat')
]