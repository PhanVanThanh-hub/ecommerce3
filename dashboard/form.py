from django.forms import ModelForm, Textarea
from django import forms
from ecom.models import *
from .models import *

class addProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude= ['priceFilter']
        widgets = {
            'all': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
         
        
class updataProductForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Product.objects.all())
    price = forms.FloatField()
    amout = forms.IntegerField()

    cost = forms.FloatField()

class giftVoucherForm(ModelForm):
     class Meta:
        model = giftVoucher
        fields = '__all__'
        widgets = {
            'all': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

     

     