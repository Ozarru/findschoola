from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('enquiries', enquiries, name='enquiries'),
    path('notices', notices, name='notices'),
    path('sch_blog', sch_blog, name='sch_blog'),
    path('plans', plans, name='plans'),
    path('settings', settings, name='settings'),
    # path('', dashboard, name='notifications'),
]
