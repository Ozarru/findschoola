from django.urls import path, include
from .views import *

# app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('ads/', ads, name='ads'),
    path('post_ad/', post_ad, name='post_ad'),
    path('ads/<str:pk/', update_ad, name='update_ad'),
    path('ccm/', ccm, name='ccm'),
    path('faq/', faq, name='faq'),
    path('tariff/', tariff, name='tariff'),
    path('notfound/', notfound, name='notfound'),
    path('new_ad/', AdvertCreateView.as_view(), name='post_demand'),
    path('new_ad/', AdvertUpdateView.as_view(), name='post_offer'),
]
