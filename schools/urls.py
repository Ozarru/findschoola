from django.urls import path, include
from .views import *

urlpatterns = [
    path('', schools, name='schools'),
    path('my_school/', mySchoolView, name='my_school'),
    path('add_school/<str:pk>/', add_school, name='add_school'),
    path('new/', SchoolCreateView.as_view(), name='create-school'),
    path('<str:pk>/update/', SchoolUpdateView.as_view(), name='update-school'),
    path('<str:pk>/', school, name='school'),
]
