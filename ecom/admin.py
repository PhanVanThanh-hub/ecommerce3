from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shiping)
admin.site.register(FavoriteProduct)
admin.site.register(DataOrder)
admin.site.register(Data)
 
admin.site.register(oldPassWord)
admin.site.register(Comment)
admin.site.register(LoginAttempts)
admin.site.register(Income)
admin.site.register(Bill)
# class ClientAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}

# admin.site.register(Category, ClientAdmin)