from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

# Create your models here.


class Blogpost(models.Model):

    image = models.ImageField(
        upload_to='blog', blank=True, null=True)
    title = models.CharField(max_length=255, default='')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, default='')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost', kwargs={'pk': self.pk})
