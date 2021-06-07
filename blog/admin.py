from django.contrib import admin
from .models import *
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug': ('name',)}
admin.site.register(Blog,ClientAdmin)
admin.site.register(Category,ClientAdmin)