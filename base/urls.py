from django.urls import path, include
from .views import *

# app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('ads/', ads, name='ads'),
    path('ccm/', ccm, name='ccm'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('tariff/', tariff, name='tariff'),
    path('notfound/', notfound, name='notfound'),
]
