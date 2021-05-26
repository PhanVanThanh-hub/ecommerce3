# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/productDetail/(?P<room_name>\w+)/$', consumers.CmtConsumer.as_asgi()),
]