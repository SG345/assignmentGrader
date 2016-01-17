from django.shortcuts import render
from django import forms
from portal import models
from portal.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    navbar="navbar.html"


    regStatus = False

    if request.method == 'POST':
        #grab info from raw information
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()

            #hash the password for security using the djangohash default method
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile_pic = request.FILES['profile_pic']
            profile.save()

            regStatus = True

        else:
            print user_form.errors, profile_form.errors
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': regStatus})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect('landing')
        else:
            return HttpResponse('Invalid login credentials')

    else:
        return render(request, 'login.html', {})


def logout_me(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def homepage(request):
    return render(request, 'home.html', {})

def show_problems(request):
    from portal.models import Problems
    F=Problems.objects.all()
    return render(request, 'student_home.html', {'P': F})

def show_an(request):
    from portal.models import Announcements
    G=Announcements.objects.all()
    return render(request, 'an.html', {'Q': G})
