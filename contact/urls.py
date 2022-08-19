from django.urls import path, include
from .views import *

# app_name = 'base'
urlpatterns = [
    path('', contact, name='contact'),
]
