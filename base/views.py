from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from blog.models import Blogpost
from .models import Demand, Offer
from .forms import *
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
    demands = Demand.objects.all()
    offers = Offer.objects.all()
    blogposts = Blogpost.objects.all()
    schools = School.objects.filter(
        Q(name__icontains=query) | Q(address__icontains=query))
    context = {
        "home_page": "active",
        'schools': schools,
        'edu_levels': edu_levels,
        'demands': demands,
        'offers': offers,
        'has_school': has_school,
        'blogposts': blogposts,
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


@login_required(login_url='login')
def post_ad(req):

    print(req.user.username)
    form = AdvertForm(initial={'author': req.user})
    if req.method == 'POST':
        if form.is_valid():
            print(req.user.username)
            form.save()
            return redirect('ads')

    context = {
        "post_ad_page": "active",
        'form': form,
        "title": 'post_ad',
    }
    return render(req, 'base/post_ad.html', context)


@login_required(login_url='login')
def update_ad(req):
    demForm = DemandForm(initial={'author': req.user})
    if req.method == 'POST':
        print(req.POST)
        form = DemandForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('ads')


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
    fields = '__all__'
    exclude = ('author', 'date_added')

    def form_valid(self, form):
        form.instance.author = self.request.user
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
