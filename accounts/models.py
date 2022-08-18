from sys import maxsize
from django.contrib.auth.models import AbstractUser
from django.db import models


role_choices = (('utilisateur', 'Utilisateur générique'),
                ('gestionaire', "Gestionaire d'école"),)

subrole_choices = (('admin', 'School Admin'),
                   ('editor', "School Editor"),)


class CustomUser(AbstractUser):
    pass
    email = models.CharField(verbose_name='email',
                             max_length=128, unique=True)
    role = models.CharField(max_length=50, blank=True,
                            null=True, choices=role_choices)
    subrole = models.CharField(
        max_length=50, blank=True, null=True, choices=subrole_choices)
    tel = models.CharField(max_length=20, blank=True, null=True)
    profile_img = models.ImageField(
        upload_to='accounts/profiles', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.username}(role: {self.role})(subrole: {self.subrole})'
