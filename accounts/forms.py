from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email",
                  "password1", "password2",
                  "first_name",
                  "last_name", "tel",
                  "profile_img",
                  "role")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            "profile_img",
            "username",
            "email",
            "first_name",
            "last_name", "tel", "role", "subrole")

        exclude = ("password", )
