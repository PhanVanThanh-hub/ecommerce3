from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User
from django import forms
from .models import *


class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude =['user']

class changePassWordForm(forms.Form):
    path = forms.CharField(required=False)
    currentPassword = forms.CharField(required=True,max_length=100)
    newPassword = forms.CharField(max_length=100)
    confirmPassword = forms.CharField(max_length=100)

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
     

     