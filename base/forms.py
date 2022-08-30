from django import forms
from .models import *


class AdvertForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control mb-4"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control mb-4", "rows": 20}))

    class Meta:
        model = Advert
        fields = ['title', 'content']
