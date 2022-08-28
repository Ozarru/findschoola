from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from base.models import Demand
from .forms import *
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    fields = (
        "image",
        "username",
        "email",
        "first_name",
        "last_name", "tel", "role", "subrole")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        school = self.get_object()
        if self.request.user == CustomUser:
            return True
        return False


def signupView(req):
    form = CustomUserCreationForm(req.POST)
    if req.user.is_authenticated:
        return redirect('home')

    if req.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(req, "Votre compte vien d'être créé.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {
        "signup_page": "active", "title": "signup", "form": form}
    return render(req, 'accounts/signup.html', context)


def loginView(req):
    if req.user.is_authenticated:
        return redirect('home')

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            messages.info(req, 'Username or Password is incorrect!')
    context = {
        "login_page": "active",
        "title": 'login'}
    return render(req, 'accounts/login.html', context)


@login_required(login_url='login')
def logoutUser(req):
    logout(req)
    return redirect('home')


@login_required(login_url='login')
def userprofile(req):
    # user = CustomUser.objects.get(id=pk)
    # if user.id != pk:
    #     return redirect(f'/')
    demands = Demand.objects.all()
    form = CustomUserChangeForm(instance=req.user)
    # p_form = ProfileForm(instance=req.user.profile)
    if req.method == 'POST':
        form = CustomUserChangeForm(req.POST, instance=req.user)
        # p_form = ProfileForm(req.POST, req.FILES, instance=req.user.profile)

        if form.is_valid():
            # if form.is_valid() and p_form.is_valid():
            form.save()
            # p_form.save()
            messages.success(req, "Votre compte vien d'être modifié.")
            return redirect(f'profile')
    context = {
        "profile_page": "active",
        "demands": demands,
        "title": 'profile',
        "form": form,
        # "p_form": p_form
    }
    return render(req, 'accounts/user_profile.html', context)
