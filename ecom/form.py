from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User
from django import forms
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude =['user']

class ChangePassWordForm(forms.Form):
    path = forms.CharField(required=False)
    currentPassword = forms.CharField(required=True,max_length=100)
    newPassword = forms.CharField(max_length=100)
    confirmPassword = forms.CharField(max_length=100)


     

     