from django.forms import ModelForm, Textarea
from django import forms
from ecom.models import *
from .models import *

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude= ['priceFilter','sold']
        widgets = {
            'all': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
         
        
class UpdataProductForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Product.objects.all())
    price = forms.FloatField()
    amout = forms.IntegerField()

    cost = forms.FloatField()

class GiftVoucherForm(ModelForm):
     class Meta:
        model = giftVoucher
        fields = '__all__'
        widgets = {
            'all': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

from blog.models import *

class AddBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
   
        # widgets = {
        #     'all': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
         