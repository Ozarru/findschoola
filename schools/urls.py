from django.urls import path, include
from .views import *

urlpatterns = [
    path('', schools, name='schools'),
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('sch_list/', sch_list, name='sch_list'),
    path('create/', create_school, name='create_school'),
    path('edit/', edit_school, name='edit_school'),
    path('my_school/', mySchool, name='my_school'),
    path('<str:pk>/articles/', articles, name='sch_articles'),
    path('<str:pk>/', school, name='school'),
    # path('<str:pk>/levels_mod/', levelsMod, name='levels_mod'),
]
