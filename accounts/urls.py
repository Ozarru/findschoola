from django.urls import path

from .views import *

urlpatterns = [
    path('login/', loginView, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', signupView, name='signup'),
    path('profile/', userprofile, name='profile'),
    path('profile/<str:pk>/update/',
         UserUpdateView.as_view(), name='update-profile'),
]
