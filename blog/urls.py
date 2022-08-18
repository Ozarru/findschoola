from django.urls import path, include
from .views import *

# app_name = 'base'
urlpatterns = [
    path('', blog, name='blog'),
    path('<str:pk>/', blogpost, name='blogpost'),
]
