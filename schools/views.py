import json
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import SchoolCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    # form = SchoolCreationForm
    fields = ('crest', 'thumbnail', 'banner', 'name', 'email', 'website', 'address',
              'tel', 'cel', 'moto', 'year_founded', 'resumption')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SchoolUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = School
    # form = SchoolCreationForm
    fields = ('crest', 'thumbnail', 'banner', 'name', 'email', 'website', 'address',
              'tel', 'cel', 'moto', 'year_founded', 'resumption')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        school = self.get_object()
        if self.request.user == school.user:
            return True
        return False


@login_required(login_url='login')
def add_school(req, pk):
    user = CustomUser.objects.get(id=pk)
    form = SchoolCreationForm
    if req.method == 'POST':
        form = SchoolCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "add_school_page": "active", "title": 'add_school', "form": form}
    return render(req, 'schools/add_school.html', context)


@login_required(login_url='login')
def mySchoolView(req, pk):
    context = {
        "my_school_page": "active", "title": 'my_school'}
    return render(req, 'schools/my_school.html', context)


def schools(req):
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    schools = School.objects.filter(
        Q(name__icontains=query) | Q(address__icontains=query) | Q(
            moto__icontains=query) | Q(tel__icontains=query)
    )
    edu_levels = EduLevel.objects.all()
    # for school in schools:
    #     sch_levels = school.edu_levels_set.all()
    ordering = ['is_featured == True']
    context = {
        "schools_page": "active",
        'title': 'schools',
        'schools': schools,
        'edu_levels': edu_levels,
        # 'sch_levels': [sch_levels],
        'ordering': ordering,
    }

    return render(req, 'schools/index.html', context)


def school(req, pk):
    school = School.objects.get(id=pk)
    # people
    teachers = school.teacher_set.all()
    # structures
    libraries = school.library_set.all()
    canteens = school.canteen_set.all()
    laboratories = school.laboratory_set.all()
    classrooms = school.classroom_set.all()
    # information
    reports = school.report_set.all()
    advantages = school.advantage_set.all()

    context = {
        "schools_page": "active",
        'title': 'school',
        'school': school,
        'teachers': teachers,
        'classrooms': classrooms,
        'laboratories': laboratories,
        'libraries': libraries,
        'canteens': canteens,
        'reports': reports,
        'advantages': advantages
    }
    return render(req, 'schools/detail.html', context)
