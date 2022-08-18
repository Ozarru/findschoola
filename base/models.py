from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from schools.models import School


class Demand(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username


class Offer(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
#
