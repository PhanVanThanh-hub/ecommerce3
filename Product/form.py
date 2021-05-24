from django.forms import ModelForm, Textarea
from django import forms
from ecom.models import *

class commentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows":6, "cols":75}),max_length=1000)

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
     

     