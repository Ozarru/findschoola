from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


role_choices = (('utilisateur', 'Utilisateur générique (Parent/Eleve)'),
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
    image = models.ImageField(default='anonuser.jpg',
                              upload_to='users', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.username}(role: {self.role})(subrole: {self.subrole})'


# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     image = models.ImageField(default='anon.jpg',
#                               upload_to='users', blank=True, null=True)

#     def __str__(self):
#         return f'{self.user.username} Profile picture'

#     def save(self):
#         super().save()

#         img = Image.open(self.image.path)
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
