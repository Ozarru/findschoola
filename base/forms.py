from django.forms import ModelForm
from .models import *


class DemandForm(ModelForm):

    class Meta:
        model = Demand
        fields = '__all__'
        exclude = ('author', 'date_added')


class OfferForm(ModelForm):

    class Meta:
        model = Offer
        fields = '__all__'
        exclude = ('author', 'date_added')


class AdvertForm(ModelForm):

    class Meta:
        model = Advert
        fields = '__all__'
        exclude = ('author', 'date_added')
