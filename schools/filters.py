from cProfile import label
from xml.dom.minidom import Attr
import django_filters
from .models import *
from django_filters import CharFilter


class SchoolFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(
    #     field_name='name',
    #     lookup_expr='icontains', label='',)
    # address = django_filters.CharFilter(
    #     field_name='address',
    #     lookup_expr='icontains', label='')
    # levels = django_filters.CharFilter(
    #     field_name='levels',
    #     lookup_expr='iexact', label='',)

    class Meta:
        model = School
        # fields = ['name', 'address', 'levels']
        fields = {'name': ['icontains'], 'address': [
            'icontains'], 'levels': ['iexact'], }
