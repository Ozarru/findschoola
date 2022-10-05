import logging
from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import SchoolForm


@login_required(login_url='login')
def create_school(req):
    user = req.user
    has_school = School.objects.get(manager=user)
    if user.role != 'manager':
        return redirect('home')

    if has_school:
        return redirect('home')

    if req.method == 'POST':
        form = SchoolForm(req.POST)
        form.instance.manager = user
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "sch_profile_page": "active", "title": 'add_school', "user": user, "form": form}
    return render(req, 'schools/school_form.html', context)


@login_required(login_url='login')
def edit_school(req):
    user = req.user
    school = School.objects.get(manager=user)
    if not school and user.role != 'manager':
        return redirect('home')

    form = SchoolForm(instance=school)
    if req.method == 'POST':
        form = SchoolForm(req.POST, instance=school)
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "sch_profile_page": "active", "title": 'add_school', "school": school, "user": user, "form": form}
    return render(req, 'schools/school_form.html', context)


def schools(req):
    has_school = False
    user = req.user
    if user.is_authenticated:
        school = School.objects.filter(manager=user)
        if school:
            has_school = True
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    schools = School.objects.filter(
        Q(name__icontains=query)
        | Q(address__icontains=query)
        | Q(moto__icontains=query)
        | Q(tel__icontains=query)
        | Q(levels__name__icontains=query)
    ).distinct()

    # # ------------------ dropdown filter
    # all_schools = School.objects.all()
    # school_filter = SchoolFilter(req.GET, queryset=all_schools)

    edu_levels = EduLevel.objects.all()
    ordering = ['is_featured == True']
    context = {
        "schools_page": "active",
        'title': 'schools',
        'schools': schools,
        'edu_levels': edu_levels,
        "has_school": has_school,
        # "school_filter": school_filter,
        'ordering': ordering,
    }
    print(edu_levels)
    return render(req, 'schools/index.html', context)


def school(req, pk):
    is_manager = False
    user = req.user
    school = School.objects.get(id=pk)

    if user == school.manager:
        is_manager = True

    # people
    teachers = school.teacher_set.all()
    # structures
    classrooms = school.classroom_set.all()
    structures = school.structure_set.all()
    # information
    articles = school.article_set.all()
    advantages = school.advantage_set.all()
    levels = EduLevel.objects.all()

    context = {
        "schools_page": "active",
        'title': 'school',
        'school': school,
        'teachers': teachers,
        'classrooms': classrooms,
        'structures': structures,
        'is_manager': is_manager,
        'articles': articles,
        'levels': levels,
        'advantages': advantages
    }
    return render(req, 'schools/detail.html', context)


@login_required(login_url='login')
def mySchool(req):
    is_manager = False
    user = req.user
    school = School.objects.get(manager=user)
    if not school and user.role != 'manager':
        return redirect('home')
    else:
        is_manager = True

    # people
    teachers = school.teacher_set.all()
    # structures
    classrooms = school.classroom_set.all()
    structures = school.structure_set.all()
    # information
    articles = school.article_set.all()
    advantages = school.advantage_set.all()
    levels = EduLevel.objects.all()

    context = {
        "schools_page": "active",
        'title': 'school',
        'school': school,
        'teachers': teachers,
        'classrooms': classrooms,
        'structures': structures,
        'is_manager': is_manager,
        'articles': articles,
        'levels': levels,
        'advantages': advantages
    }
    return render(req, 'schools/detail.html', context)


@login_required(login_url='login')
def articles(req, pk):
    is_manager = False
    school = School.objects.get(id=pk)
    # people
    articles = school.article_set.all()

    context = {
        "schools_page": "active",
        'title': 'school',
        'school': school,
        'is_manager': is_manager,
        'articles': articles,
    }
    return render(req, 'schools/articles.html', context)


@login_required(login_url='login')
def levelsMod(req, pk):
    is_manager = False
    user = req.user
    if user.is_authenticated:
        school = School.objects.get(manager=user, id=pk)
        if school:
            is_manager = True

    all_levels = EduLevel.objects.all()
    context = {
        "schools_page": "active",
        'title': 'levels_mod',
        'school': school,
        'all_levels': all_levels,
    }
    # user = req.user
    # if user.is_authenticated:
    #     school = School.objects.filter(manager=user, id=pk)
    #     if school:
    #         is_manager = True

    if not is_manager:
        return redirect('home')

    if req.method == 'POST':
        if req.POST.get('levels'):
            school.levels.set(req.POST.get('levels').id)
            school.save()
            return redirect('my_school')
    else:
        return render(req, 'schools/levels_mod.html', context)
