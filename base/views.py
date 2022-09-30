from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from blog.models import Blogpost
from .forms import *
from django.urls import reverse_lazy
from schools.models import EduLevel, School
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView


def home(req):
    # schools = data['schools']
    has_school = False
    user = req.user
    if user.is_authenticated:
        school = School.objects.filter(manager=user)
        if school:
            has_school = True

    query = req.GET.get('query') if req.GET.get('query') != None else ''
    edu_levels = EduLevel.objects.all()
    adverts = Advert.objects.all()
    blogposts = Blogpost.objects.all()
    schools = School.objects.filter(
        Q(name__icontains=query) | Q(address__icontains=query))
    count_creches = School.objects.filter(levels=1).count()
    count_jardins = School.objects.filter(levels=2).count()
    count_primaires = School.objects.filter(levels=3).count()
    count_colleges = School.objects.filter(levels=4).count()
    count_lycees = School.objects.filter(levels=5).count()
    count_universites = School.objects.filter(levels=6).count()
    count_academiques = School.objects.filter(levels=7).count()
    count_professionels = School.objects.filter(levels=8).count()
    context = {
        "home_page": "active",
        'schools': schools,
        'edu_levels': edu_levels,
        'adverts': adverts,
        'has_school': has_school,
        'blogposts': blogposts,
        'count_creches': count_creches,
        'count_jardins': count_jardins,
        'count_primaires': count_primaires,
        'count_colleges': count_colleges,
        'count_lycees': count_lycees,
        'count_professionels': count_professionels,
        'count_academiques': count_academiques,
        'count_universites': count_universites,
        'title': 'schools'}
    return render(req, 'base/index.html', context)


def about(req):
    context = {
        "about_page": "active",
        "title": 'about'}
    return render(req, 'base/about.html', context)


def ads(req):
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    # demands = Demand.objects.filter(
    #     Q(title__icontains=query) | Q(date_added__icontains=query))
    # offers = Offer.objects.filter(
    #     Q(title__icontains=query) | Q(date_added__icontains=query))
    adverts = Advert.objects.filter(
        Q(title__icontains=query) | Q(date_added__icontains=query))

    context = {
        "ads_page": "active",
        # "offers": offers,
        # "demands": demands,
        "adverts": adverts,
        "title": 'ads',
    }
    return render(req, 'base/ads.html', context)


def ccm(req):
    context = {
        "ccm_page": "active",
        "title": 'ccm', }
    return render(req, 'base/ccm.html', context)


def notfound(req):
    context = {
        "notfoud_page": "active",
        "title": 'notfound', }
    return render(req, 'base/notfound.html', context)


def faq(req):
    context = {
        "faq_page": "active",
        "title": 'faq'}
    return render(req, 'base/faq.html', context)


def copyrights(req):
    context = {
        "copy_page": "active",
        "title": 'copyrights', }
    return render(req, 'base/copyrights.html', context)


def privacy_policy(req):
    context = {
        "privacy_policy_page": "active",
        "title": 'privacy_policy', }
    return render(req, 'base/privacy_policy.html', context)


def terms_of_use(req):
    context = {
        "terms_of_use_page": "active",
        "title": 'terms_of_use', }
    return render(req, 'base/terms_of_use.html', context)


def limitation_of_liability(req):
    context = {
        "limitation_of_liability_page": "active",
        "title": 'limitation_of_liability', }
    return render(req, 'base/limitation_of_liability.html', context)


def tariff(req):
    if req.user.is_authenticated is False or req.user.role != 'gestionaire':
        return redirect('home')

    context = {
        "tariff_page": "active",
        "title": 'tariff'}
    return render(req, 'base/tariff.html', context)

# -------------------------


class AdvertCreateView(LoginRequiredMixin, CreateView):
    model = Advert
    fields = ('title', 'content')
    success_url: reverse_lazy('ads')

    def form_valid(self, form):
        if self.request.user.role == 'gestionaire':
            form.instance.author = self.request.user
            form.instance.ad_type = 'offer'
            return super().form_valid(form)
        else:
            form.instance.author = self.request.user
            form.instance.ad_type = 'demand'
            return super().form_valid(form)


class AdvertUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advert
    fields = '__all__'
    exclude = ('author', 'date_added')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        advert = self.get_object()
        if self.request.user == advert.author:
            return True
        return False
