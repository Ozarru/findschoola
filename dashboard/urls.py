from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('enquiries', enquiries, name='enquiries'),
    path('notices', notices, name='notices'),
    path('articles', articles, name='articles'),
    path('teachers', teachers, name='teachers'),
    path('classes', classes, name='classes'),
    path('structures', structures, name='structures'),
    path('plans', plans, name='plans'),
    path('settings', settings, name='settings'),
    # path('', dashboard, name='notifications'),
]
