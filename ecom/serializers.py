from rest_framework import serializers
from .models import  *

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Discount
		fields ='__all__'

 

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
		 
	 