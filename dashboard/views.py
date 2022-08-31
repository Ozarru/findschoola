from accounts.models import CustomUser
from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import *


@login_required(login_url='login')
def dashboard(req):
    context = {
        "dash_page": "active", "title": 'dashboard'}
    return render(req, 'dashboard/index.html', context)


@login_required(login_url='login')
def settings(req):
    context = {
        "settings_page": "active", "title": 'settings'}
    return render(req, 'dashboard/settings.html', context)


@login_required(login_url='login')
def enquiries(req):
    context = {
        "enquiries_page": "active", "title": 'enquiries'}
    return render(req, 'dashboard/enquiries.html', context)


@login_required(login_url='login')
def notices(req):
    context = {
        "notices_page": "active", "title": 'notices'}
    return render(req, 'dashboard/notices.html', context)


@login_required(login_url='login')
def sch_blog(req):
    context = {
        "sch_blog_page": "active", "title": 'bulletin'}
    return render(req, 'dashboard/bulletin.html', context)


@login_required(login_url='login')
def plans(req):
    context = {
        "plans_page": "active", "title": 'plans'}
    return render(req, 'dashboard/plans.html', context)
