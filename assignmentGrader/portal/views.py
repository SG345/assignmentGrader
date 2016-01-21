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
    ans_code = "abc"
    regStatus = False
    from django.contrib.auth.models import User


    if request.method == 'POST':
        #grab info from raw information
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        #if user_form.is_valid() and profile_form.is_valid():
            #user=user_form.save()

            #hash the password for security using the djangohash default method
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        secret_code = request.POST.get('secret_code')
        staffval = False
        if secret_code == ans_code:
            staffval = True

            #user.set_password('user.password')
        user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

        user.save()
        user.set_password(password)
        if staffval == True:
            user.is_staff=True

        user.save()
            #profile = profile_form.save(commit=False)
            #profile.user = user

            #if 'profile_pic' in request.FILES:
             #   profile_pic = request.FILES['profile_pic']
            #profile.save()

        regStatus = True

    return render(request, 'home.html', {})
def show_reg_form(request):
    return render(request, 'register.html', {})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            if user.is_staff==True:
                return HttpResponseRedirect('/portal/staff_home')

            return HttpResponseRedirect('landing')
        else:
            return HttpResponse('Invalid login credentials')

    else:
        return render(request, 'login.html', {})


def add_problem(request):
    from portal.models import Problems 
    if request.method == 'POST':
        pdes = request.POST.get('pdes')
        ptitle = request.POST.get('ptitle')
        ptest = request.POST.get('ptest')
        psource = request.POST.get('psource')
        eo = request.POST.get('eo')
        A = Problems.objects.all()
        i = 1
        for item in A:
            i = i+1


        a = Problems(problem_id=i,problem_description=pdes, problem_title=ptitle, test_cases=ptest, answer_source=psource, expected_output= eo)
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

def show_problems(request):
    from portal.models import Problems
    F=Problems.objects.all()
    return render(request, 'student_home.html', {'P': F})

def show_an(request):
    from portal.models import Announcements
    G=Announcements.objects.all()

    G.sort(reverse=True)
    return render(request, 'an.html', {'Q': G})

def add_an(request):
    from portal.models import Announcements
    if request.method == 'POST':
        an_title = request.POST.get('an_title')
        an_des = request.POST.get('an_des')
        
        A = Announcements.objects.all()
        i = 1
        for item in A:
            i = i+1


        a = Announcements(an_id=i,an_des=an_des, an_title=an_title)
        a.save()
        #return render(request, 'student_home.html', {'P': F})
        return HttpResponseRedirect('/portal/an_staff')

def DeleteThisAn(request, an_id=0):
    from portal.models import Announcements
    a=Announcements.objects.get(an_id=an_id)
    a.delete()
    return HttpResponseRedirect('/portal/an_staff')

def show_an_staff(request):
    from portal.models import Announcements
    G=Announcements.objects.all()
    return render(request, 'an_staff.html', {'Q': G})


def show_staff(request):
    from portal.models import Problems
    G=Problems.objects.all()
    return render(request, 'staff_home.html', {'P': G})


def add_prob_form(request):
    return render(request, 'add_problem.html', {})

def DeleteThisProb(request, pid=0):
    from portal.models import Problems
    a=Problems.objects.get(problem_id=pid)
    a.delete()
    return HttpResponseRedirect('/portal/staff_home')
