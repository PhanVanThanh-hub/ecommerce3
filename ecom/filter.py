import django_filters
from django_filters import DateFilter,CharFilter
from .models import *
from django.forms.widgets import TextInput
class productFilter(django_filters.FilterSet):
    start_date= DateFilter(label=('start_date'),widget=TextInput(attrs={'placeholder': 'mm/dd/yyyy'}),field_name="date_complete",lookup_expr='gte')
    end_date = DateFilter(label=('end_date'),widget=TextInput(attrs={'placeholder': 'mm/dd/yyyy'}),field_name="date_complete", lookup_expr='lte')
    class Meta:
        model = Data
        fields ='__all__'
        exclude =['dataOrder','date_complete','complete','quantity']