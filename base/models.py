from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from schools.models import School


class Demand(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Offer(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
#


advert_types = (('demand', 'Demande'),
                ('offer', "Offre"),)


class Advert(models.Model):

    ad_type = models.CharField(max_length=50, blank=True,
                               null=True, choices=advert_types, default='demand')
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
