from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('enquiries', enquiries, name='enquiries'),
    path('sch_profile', schProlile, name='sch_profile'),
    path('notices', notices, name='notices'),
    path('bulletin', bulletin, name='bulletin'),
    path('plans', plans, name='plans'),
    path('settings', settings, name='settings'),
    # path('', dashboard, name='notifications'),
    # path('', SchoolListView.as_view(), name='schools'),
    # path('<str:slug>/', SchoolDetailView.as_view(),
    #      name='school-detail'),
]
