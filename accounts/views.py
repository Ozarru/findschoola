from django.shortcuts import render, redirect

from base.models import Demand
from .forms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signupView(req):
    form = CustomUserCreationForm(req.POST)
    if req.user.is_authenticated:
        return redirect('home')

    if req.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(req, "Votre compte vien d'être créé.")
            return redirect('login')
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
def userprofile(req, pk):
    user = CustomUser.objects.get(id=pk)
    # if user.id != pk:
    #     return redirect(f'/')
    demands = Demand.objects.all()
    form = CustomUserChangeForm(instance=user)
    if req.method == 'POST':
        form = CustomUserChangeForm(req.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(req, "Votre compte vien d'être modifié.")
            return redirect(f'/')
    context = {
        "profile_page": "active",
        "user": user,
        "demands": demands,
        "title": 'profile', "form": form}
    return render(req, 'accounts/user_profile.html', context)
