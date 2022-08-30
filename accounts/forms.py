from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = ''
        self.fields["email"].help_text = ''
        self.fields["password1"].help_text = ''
        self.fields["password2"].help_text = ''

    class Meta:
        model = CustomUser
        fields = (

            "role",
            "username", "email",
            "password1", "password2",
            "first_name",
            "last_name", "tel",
            # "image",
        )
        help_texts = None


class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.fields["image"].help_text = ''
        self.fields["username"].help_text = ''

    class Meta:
        model = CustomUser
        fields = (
            # "image",
            "username",
            "email",
            "first_name",
            "last_name", "tel", "role", "subrole")

        exclude = ("password", )


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
