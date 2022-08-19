from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (

            "role",
            "username", "email",
            "password1", "password2",
            "first_name",
            "last_name", "tel", "image",)
        # help_texts = {
        #     'username': None,
        #     'email': None,
        #     'password1': None,
        #     'password2': None,
        # }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            "image",
            "username",
            "email",
            "first_name",
            "last_name", "tel", "role", "subrole")

        exclude = ("password", )


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
