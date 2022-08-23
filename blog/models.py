from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Blogpost(models.Model):

    image = models.ImageField(
        upload_to='blog', blank=True, null=True)
    title = models.CharField(max_length=255, default='News Title')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, default='News')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(auto_now=True)
