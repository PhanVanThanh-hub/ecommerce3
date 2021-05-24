from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User
from django import forms
from ecom.models import *
class CreateUserForm(UserCreationForm):
    phone = forms.CharField(required=True,max_length=10)
    class Meta:
        model = User
        fields = ['username','email','phone','password1','password2']   

    def save(self, commit=True):    
        user = super(UserCreationForm, self).save(commit=False)
        user.phone = self.cleaned_data["phone"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user