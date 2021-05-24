from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User
from django import forms
from ecom.models import *


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
     

     