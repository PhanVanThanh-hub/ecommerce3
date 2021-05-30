from rest_framework import serializers
from .models import  *

 

 

class ProductList(serializers.ModelSerializer):
	 
	class Meta:
		model = Product
		fields = '__all__'

class FooBaseSerializerLevel1(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = '__all__'

class TaskOrder(serializers.ModelSerializer):
 
	 
	class Meta:
		model = LoginAttempts
		fields = '__all__'
		 
	 