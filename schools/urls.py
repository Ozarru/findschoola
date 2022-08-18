from django.urls import path, include
from .views import *

urlpatterns = [
    path('', schools, name='schools'),
    path('my_school/', mySchoolView, name='my_school'),
    path('add_school/<str:pk>/', add_school, name='add_school'),
    path('<str:pk>/', school, name='school'),
]
