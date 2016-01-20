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


def add_problem(request):
    from portal.models import Problems 
    if request.method == 'POST':
        pid = request.POST.get('pid')
        pdes = request.POST.get('pdes')
        ptitle = request.POST.get('ptitle')
        ptest = request.POST.get('ptest')
        psource = request.POST.get('psource')
        eo = request.POST.get('eo')

        a = Problems(problem_id=pid, problem_description=pdes, problem_title=ptitle, test_cases=ptest, answer_source=psource, expected_output= eo)
        a.save()
        F=Problems.objects.all()
        #return render(request, 'student_home.html', {'P': F})
        return HttpResponseRedirect('psuccess/')


def edit_problem(request):
    from portal.models import Problems 
    if request.method == 'POST':
        pid = request.POST.get('pid')

        #a = Problems(problem_id=pid, problem_description=pdes, problem_title=ptitle, test_cases=ptest, answer_source=psource, expected_output= eo)
        #a.save()
        F=Problems.objects.all()
        for w in F:
            if w.problem_id == pid:
                return render(request, 'edit_prob.html', {'E': w})

def add_editted_prob(request):
    from portal.models import Problems 
    if request.method == 'POST':
        pid = request.POST.get('pid')
        pdes = request.POST.get('pdes')
        ptitle = request.POST.get('ptitle')
        ptest = request.POST.get('ptest')
        psource = request.POST.get('psource')
        eo = request.POST.get('eo')
        
        a = Problems.objects.get(problem_id=pid)
        a.problem_title=ptitle
        a.test_cases=ptest
        a.answer_source=psource
        a.expected_output=eo
        a.problem_description=pdes
        a.save()

        return HttpResponseRedirect('/portal/staff_home')

        #from portal.models import Problems
        #G=Problems.objects.all()
        #return render(request, 'staff_home.html', {'P': G})


def psu(request):
    return render(request, 'add_redirect.html', {})

def logout_me(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def homepage(request):
    return render(request, 'home.html', {})

def delete_prob(request):
    delete_p=request.GET.get('id','')

def show_problems(request):
    from portal.models import Problems
    F=Problems.objects.all()
    return render(request, 'student_home.html', {'P': F})

def show_an(request):
    from portal.models import Announcements
    G=Announcements.objects.all()
    return render(request, 'an.html', {'Q': G})

def show_staff(request):
    from portal.models import Problems
    G=Problems.objects.all()
    return render(request, 'staff_home.html', {'P': G})


def add_prob_form(request):
    return render(request, 'add_problem.html', {})
