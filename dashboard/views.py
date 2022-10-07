from accounts.models import CustomUser
from base.forms import AdvertForm
from base.models import Advert
from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from schools.forms import *


@login_required(login_url='login')
def dashboard(req):
    user = req.user
    school = School.objects.get(manager=user)
    teachers = Teacher.objects.filter(school=school).count()
    if not school and user.role != 'manager':
        return redirect('home')

    context = {
        "dash_page": "active", "title": 'dashboard', 'school': school, 'teachers': teachers}
    return render(req, 'dashboard/index.html', context)


@login_required(login_url='login')
def settings(req):
    context = {
        "settings_page": "active", "title": 'settings'}
    return render(req, 'dashboard/settings.html', context)


def enquiries(req):
    user_ads = Advert.objects.filter(author=req.user)
    form = AdvertForm()
    if req.method == 'POST':
        form = AdvertForm(req.POST)
        form.instance.author = req.user
        if form.is_valid():
            form.save()
            return redirect('ads')
    context = {
        "enquiries_page": "active", "title": 'user_ads', "user_ads": user_ads, "form": form}
    return render(req, 'dashboard/enquiries.html', context)


@login_required(login_url='login')
def notices(req):
    context = {
        "notices_page": "active", "title": 'notices'}
    return render(req, 'dashboard/notices.html', context)


@login_required(login_url='login')
def articles(req):
    user = req.user
    school = School.objects.get(manager=user)
    articles = Article.objects.filter(school=school)
    if not school and user.role != 'manager':
        return redirect('home')

    form = ArticleForm()
    if req.method == 'POST':
        form = ArticleForm(req.POST)
        form.instance.school = school
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "sch_articles_page": "active", "title": 'articles', "articles": articles, "form": form}
    return render(req, 'dashboard/articles.html', context)


@login_required(login_url='login')
def classes(req):
    user = req.user
    school = School.objects.get(manager=user)
    classrooms = Classroom.objects.filter(school=school)
    if not school and user.role != 'manager':
        return redirect('home')

    form = ClassroomForm()
    if req.method == 'POST':
        form = ClassroomForm(req.POST)
        form.instance.school = school
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "sch_classes_page": "active", "title": 'classrooms', "classrooms": classrooms, "form": form}
    return render(req, 'dashboard/classes.html', context)


@login_required(login_url='login')
def structures(req):
    user = req.user
    school = School.objects.get(manager=user)
    structures = Structure.objects.filter(school=school)
    if not school and user.role != 'manager':
        return redirect('home')

    form = StructureForm()
    if req.method == 'POST':
        form = StructureForm(req.POST)
        form.instance.school = school
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "sch_structures_page": "active", "title": 'structures', "structures": structures, "form": form}
    return render(req, 'dashboard/structures.html', context)


@login_required(login_url='login')
def teachers(req):
    user = req.user
    school = School.objects.get(manager=user)
    teachers = Teacher.objects.filter(school=school)
    if not school and user.role != 'manager':
        return redirect('home')

    form = TeacherForm()
    if req.method == 'POST':
        form = TeacherForm(req.POST)
        form.instance.school = school
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "sch_teachers_page": "active", "title": 'teachers', "teachers": teachers, "form": form}
    return render(req, 'dashboard/teachers.html', context)


@login_required(login_url='login')
def plans(req):
    context = {
        "plans_page": "active", "title": 'plans'}
    return render(req, 'dashboard/plans.html', context)
