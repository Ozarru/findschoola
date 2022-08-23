from django.urls import path, include
from .views import *

urlpatterns = [
    path('', schools, name='schools'),
    path('new/', add_school, name='create_school'),
    path('my_school/', mySchool, name='my_school'),
    # path('new/', SchoolCreateView.as_view(), name='create-school'),
    path('<str:pk>/update/', SchoolUpdateView.as_view(), name='update-school'),
    path('<str:pk>/', school, name='school'),
]
