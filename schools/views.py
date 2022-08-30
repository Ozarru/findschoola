from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import SchoolCreationForm
from .filters import SchoolFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    fields = ('crest', 'thumbnail', 'banner', 'name', 'email', 'website', 'address',
              'tel', 'cel', 'moto', 'year_founded',)

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)


class SchoolUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = School
    fields = ('crest', 'thumbnail', 'banner', 'name', 'email', 'website', 'address',
              'tel', 'cel', 'moto', 'year_founded', 'resumption')

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def test_func(self):
        school = self.get_object()
        if self.request.user == school.manager:
            return True
        return False


@login_required(login_url='login')
def add_school(req):
    user = req.user
    has_school = School.objects.filter(manager=user)
    if user.role != 'gestionaire':
        return redirect('home')

    if has_school:
        return redirect('home')

    form = SchoolCreationForm
    if req.method == 'POST':
        form = SchoolCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "add_school_page": "active", "title": 'add_school', "user": user, "form": form}
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
    if user.is_authenticated:
        school = School.objects.filter(manager=user, id=pk)
        if school:
            is_manager = True

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
        'is_manager': is_manager,
        'reports': reports,
        'advantages': advantages
    }
    return render(req, 'schools/detail.html', context)


@login_required(login_url='login')
def mySchool(req):
    school = School.objects.get(manager=req.user)
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
        "title": 'my_school',
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
