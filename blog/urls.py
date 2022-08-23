from django.urls import path, include
from .views import *

# app_name = 'base'
urlpatterns = [
    path('', blog, name='blog'),
    path('new/', BlogpostCreateView.as_view(), name='create-blogpost'),
    path('<str:pk>/', blogpost, name='blogpost'),
    path('<str:pk>/update/', BlogpostUpdateView.as_view(), name='update-blogpost'),
]
