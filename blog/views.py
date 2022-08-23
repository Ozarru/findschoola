from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import Blogpost

# Create your views here.


class BlogpostCreateView(LoginRequiredMixin, CreateView):
    model = Blogpost
    fields = ('image', 'title', 'subtitle', 'content',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogpostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blogpost
    fields = ('image', 'title', 'subtitle', 'content',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blogpost = self.get_object()
        if self.request.user == blogpost.author:
            return True
        return False


def blog(req):
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    blogposts = Blogpost.objects.filter(
        Q(title__icontains=query) | Q(subtitle__icontains=query))
    context = {
        "blog_page": "active",
        'blogposts': blogposts, 'title': 'blog'}
    return render(req, 'blog/index.html', context)


def blogpost(req, pk):
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    mainpost = Blogpost.objects.get(id=pk)
    otherposts = Blogpost.objects.filter(
        Q(title__icontains=query) | Q(subtitle__icontains=query))
    context = {
        "blogpost_page": "active",
        "mainpost": mainpost,
        'otherposts': otherposts,
        'title': 'blogpost'}
    return render(req, 'blog/detail.html', context)
