from accounts.models import CustomUser
from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required(login_url='login')
def dashboard(req):
    context = {
        "dash_page": "active", "title": 'dashboard'}
    return render(req, 'dashboard/index.html', context)


@login_required(login_url='login')
def schProlile(req):
    school = School.objects.get(user=req.user)

    if not school:
        return redirect('schools')

    profile_form = ProfileForm(instance=school)
    if req.method == 'POST':
        profile_form = ProfileForm(req.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('my_school')

    detail_form = DetailForm(instance=school)
    if req.method == 'POST':
        detail_form = DetailForm(req.POST)
        if detail_form.is_valid():
            detail_form.save()
            return redirect('my_school')

    academia_form = AcademiaForm(instance=school)
    if req.method == 'POST':
        academia_form = AcademiaForm(req.POST)
        if academia_form.is_valid():
            academia_form.save()
            return redirect('my_school')

    structure_form = StuctureForm(instance=school)
    if req.method == 'POST':
        structure_form = StuctureForm(req.POST)
        if structure_form.is_valid():
            structure_form.save()
            return redirect('my_school')

    context = {
        "sch_profile_page": "active", "title": 'add_school',
        "profile_form": profile_form,
        "detail_form": detail_form,
        "academia_form": academia_form,
        "structure_form": structure_form,
    }
    return render(req, 'dashboard/sch_profile.html', context)


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
def bulletin(req):
    context = {
        "bulletin_page": "active", "title": 'bulletin'}
    return render(req, 'dashboard/bulletin.html', context)


@login_required(login_url='login')
def plans(req):
    context = {
        "plans_page": "active", "title": 'plans'}
    return render(req, 'dashboard/plans.html', context)
