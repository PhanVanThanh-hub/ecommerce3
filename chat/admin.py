from ecom.models import Comment
from django.contrib import admin

from .models import *

admin.site.register(Message)
admin.site.register(Room)