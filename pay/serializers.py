from rest_framework import serializers
from pay.models import  *

class discountList1(serializers.ModelSerializer):
	class Meta:
		model = Discount
		fields = '__all__'