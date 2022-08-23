from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Nom', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    subject = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Sujet', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Message', 'class': 'form-control', "style": "height: 200px"}))
