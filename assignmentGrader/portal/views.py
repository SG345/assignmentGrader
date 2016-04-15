from django.shortcuts import render
from django import forms
from portal import models
from portal.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
def do_cmp(f1, f2):
    bufsize = 8*1024
    fp1 = open(f1, 'rb')
    fp2 = open(f2, 'rb')
    while True:
        b1 = fp1.read(bufsize)
        b2 = fp2.read(bufsize)
        if not is_same(b1, b2):
            return False
        if not b1:
            return True

def is_same(text1, text2):
    return text1.replace("\n","") == text2.replace("\n","")
# auth
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
            fail = "Invalid login credentials. Please try again or contact admin for help."
            return render(request, 'home.html', {"err": fail})
            #return HttpResponse('Invalid login credentials')

    else:
        return render(request, 'login.html', {})

def logout_me(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def homepage(request):
    return render(request, 'home.html', {})  



#announcement

def show_an(request):
    from portal.models import Announcements
    G=Announcements.objects.all()
    return render(request, 'an.html', {'Q': G})

def add_an(request):
    from portal.models import Announcements
    if request.method == 'POST':
        an_title = request.POST.get('an_title')
        an_des = request.POST.get('an_des')
     
        F = Announcements(an_des=an_des, an_title=an_title)
        F.save()
        #return render(request, 'student_home.html', {'P': F})
        return HttpResponseRedirect('/portal/an_staff')

def DeleteThisAn(request, an_id=0):
    from portal.models import Announcements
    a=Announcements.objects.get(an_id=an_id)
    a.delete()
    return HttpResponseRedirect('/portal/an_staff')

def show_an_staff(request):
    from portal.models import Announcements
    G=Announcements.objects.order_by('-an_id')
    return render(request, 'an_staff.html', {'Q': G})




#staff
def add_problem(request):
    from portal.models import Problems 
    if request.method == 'POST':
        pdes = request.POST.get('pdes')
        ptitle = request.POST.get('ptitle')
        ptest = request.POST.get('ptest')
        psource = request.POST.get('psource')
        submit_lang = request.POST.get('submit_lang')
    

        OUTPUT ="Invalid output"
        STATUS=""
        with open("test.txt", "w") as text_file:
            text_file.write(ptest)
   
        import subprocess
        if submit_lang == "c":
            with open("temp.c", "w") as text_file:
                text_file.write(psource)
            if subprocess.call(["gcc", "temp.c"]) == 0:
                subprocess.call(["./a.out <test.txt >output.txt"], shell=True)
                STATUS = "COMPILED SUCCESSFULLY"
                with open('output.txt', 'r') as myfile:
                    OUTPUT=myfile.read().replace('\n', '')

            else: STATUS = "Compilation error"

        # check whether the result is correct {}
        if submit_lang == "cpp":
            with open("test.cpp", "w") as text_file:
                text_file.write(psource)
            if subprocess.call(["g++", "test.cpp"]) == 0:
                subprocess.call(["./a.out <test.txt >output.txt"], shell=True)
                STATUS = "COMPILED SUCCESSFULLY"
                with open('output.txt', 'r') as myfile:
                    OUTPUT=myfile.read().replace('\n', '')

            else: STATUS = "Compilation error"

         

        eo = ""
        if STATUS == "Compilation Error":
            eo = "CE"
        else:
            eo = OUTPUT
        A = Problems.objects.all()
      


        a = Problems(problem_description=pdes, problem_title=ptitle, test_cases=ptest, answer_source=psource, expected_output= eo)
        a.save()
        F=Problems.objects.all()
        #return render(request, 'student_home.html', {'P': F})
        return HttpResponseRedirect('psuccess/')






def add_editted_prob(request):
    from portal.models import Problems 
    if request.method == 'POST':
        pid = request.POST.get('pid')
        pdes = request.POST.get('pdes')
        ptitle = request.POST.get('ptitle')
        ptest = request.POST.get('ptest')
        psource = request.POST.get('psource')
        #eo = request.POST.get('eo')
        submit_lang=request.POST.get('submit_lang')
       

        OUTPUT ="Invalid output"
        STATUS=""
        

        with open("test.txt", "w") as text_file:
            text_file.write(ptest)
   
        import subprocess
        if submit_lang == "c":
            with open("temp.c", "w") as text_file:
                text_file.write(psource)
            if subprocess.call(["gcc", "temp.c"]) == 0:
                subprocess.call(["./a.out <test.txt >output.txt"], shell=True)
                STATUS = "COMPILED SUCCESSFULLY"
                with open('output.txt', 'r') as myfile:
                    OUTPUT=myfile.read().replace('\n', '')

            else: STATUS = "Compilation error"

        # check whether the result is correct {}
        elif submit_lang == "cpp":
            with open("test.cpp", "w") as text_file:
                text_file.write(psource)
            if subprocess.call(["g++", "test.cpp"]) == 0:
                subprocess.call(["./a.out <test.txt >output.txt"], shell=True)
                STATUS = "COMPILED SUCCESSFULLY"
                with open('output.txt', 'r') as myfile:
                    OUTPUT=myfile.read().replace('\n', '')

            else: STATUS = "Compilation error"

         

        eo = ""
        if STATUS == "Compilation Error":
            eo = "CE"
        else:
            eo = OUTPUT
        A = Problems.objects.all()
      
        a = Problems.objects.get(problem_id=pid)
        a.problem_title=ptitle
        a.test_cases=ptest
        a.answer_source=psource
        

        a.expected_output=OUTPUT
        a.problem_description=pdes
        a.save()

       # a = Problems(problem_description=pdes, problem_title=ptitle, test_cases=ptest, answer_source=psource, expected_output= OUTPU)
       
        #return render(request, 'student_home.html', {'P': F})



        return HttpResponseRedirect('/portal/staff_home')

        #from portal.models import Problems
        #G=Problems.objects.all()
        #return render(request, 'staff_home.html', {'P': G})


def psu(request):
    return render(request, 'add_redirect.html', {})

def edit_problem(request):
    from portal.models import Problems 
    if request.method == 'POST':
        pid = request.POST.get('pid')

        #a = Problems(problem_id=pid, problem_description=pdes, problem_title=ptitle, test_cases=ptest, answer_source=psource, expected_output= eo)
        #a.save()
        F=Problems.objects.get(problem_id=pid)
        return render(request, 'edit_prob.html', {'E': F})

@login_required
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









#student

def show_problems(request):
    from portal.models import Problems
    F=Problems.objects.all()
    return render(request, 'student_home.html', {'P': F})

def show_ind_problem(request,problem_id=0):
    from portal.models import Problems
    a=Problems.objects.get(problem_id=problem_id)
    return render(request,'submit_code.html', {'SRC': a})

def submit_status(request,problem_id=0):
    if request.method == 'POST':
        submit_source = request.POST.get('submit_source')
        submit_lang = request.POST.get('submit_lang')
        submit_user = request.POST.get('submit_user')
    

        from portal.models import Problems, Submissions, Restrictions, leaderBoard



        c=Problems.objects.get(problem_id=problem_id)
        ans=c.expected_output 
        title=c.problem_title
        ptest = c.test_cases
        
        with open("test.txt", "w") as text_file:
            text_file.write(ptest)
        import datetime
        TIME_START = datetime.datetime.now()
        STATUS  = "EVALUATING"
        OUTPUT =""
        f = open('output.txt', 'r+')
        f.truncate()
        f.close()
   
        import subprocess
        if submit_lang == "c":

            with open("temp.c", "w") as text_file:
                text_file.write(submit_source)
            if subprocess.call(["gcc", "temp.c"]) == 0:
                subprocess.call(["./a.out <test.txt >output.txt"], shell=True)
                STATUS = "COMPILED SUCCESSFULLY"
                with open('output.txt', 'r+') as myfile:
                    OUTPUT=myfile.read().replace('\n', '')

            else: STATUS = "Compilation error"

        # check whether the result is correct {}
        else:
            with open("test.cpp", "w") as text_file:
                text_file.write(submit_source)
            if subprocess.call(["g++", "test.cpp"]) == 0:
                subprocess.call(["./a.out <test.txt >output.txt"], shell=True)
                STATUS = "COMPILED SUCCESSFULLY"
                with open('output.txt', 'r+') as myfile:
                    OUTPUT=myfile.read().replace('\n', '')

            else: STATUS = "Compilation error"
    
        
        A=Restrictions.objects.all()
        permit="yes"
        found = "false"
        cattempts=1
        
        for item in A:
            if item.userid==submit_user and item.problemId==problem_id:
                if item.attempt>=3:
                    permit="no"
                else:
                    cattempts=item.attempt
                    item.attempt=item.attempt+1
                    item.save()
                    
                found = "true"
        if found=="false":
            b=Restrictions(userid=submit_user,attempt="1",problemId=problem_id)
            f=b
            b.save()
        

        SCORE=0
        STATU = "EVALUATING"
        with open("ans.txt", "w") as text_file:
            text_file.write(ans)
        import filecmp

       # if filecmp.cmp('ans.txt', 'output.txt') == True:
        #    STATU="Correct answer"
        #else:
        #    STATU="Wrong answer"

        if do_cmp('ans.txt', 'output.txt') == True:
            STATU = "Correct answer"
        else:
            STATU = "Wrong answer"
        TIME_END = datetime.datetime.now()

        TOTAL_TIME = TIME_END - TIME_START
        if (TOTAL_TIME.total_seconds > c.expected_timelimit):
            STATU = "Wrong answer"

        B=Restrictions.objects.all()

        for item in B:
            if item.userid==submit_user and item.problemId==problem_id and item.allow=="true" and STATU=="Correct answer":
                    
                SCORE=10
                item.allow="false"
                item.save()
                S=leaderBoard(lb_user=submit_user)
                e=S.lb_score
                S.lb_score=e+SCORE
                S.save()
                

                #d=User.objects.get(username=user.username)
            
                

        #with open('output.txt', 'r') as file1:
            #with open('ans.txt', 'r') as file2:
               # same = set(file1).intersection(file2)

        #same.discard('\n')
        
        #import os
        #with open('some_output.txt', 'w') as file_out:
            #for line in same:
              #  file_out.write(line)
        #if os.stat("some_output.txt").st_size == 0 :
            #STATUS = "Wrong answer"
        #else :
            #"
        
        MSG ="Sorry, you have exceeded your attempts."
        if permit == "no":
            #STATU -> OUTPUT
    
            return render(request, 'verdict.html', {'VERDICT': MSG, 'TITLE':title, 'SCORE': SCORE})
        else:
            a = Submissions(submit_pid=problem_id, submit_verdict=STATU, submit_title=title, submit_user=submit_user, submit_lang=submit_lang, submit_source=submit_source, submit_etime=TOTAL_TIME.total_seconds())
            a.save()
            return render(request, 'verdict.html', {'SRC': a, 'VERDICT': STATU, 'TITLE':title, 'SCORE': SCORE})

@login_required
def submission_history(request):

    from portal.models import Submissions

    W = Submissions.objects.all()

    return render(request, 'submission.html', {'S':W})


def rankBoard(request):
    from portal.models import leaderBoard

    LB = leaderBoard.objects.all()

    LB=leaderBoard.objects.order_by('-lb_score')

    return render(request, 'rank.html', {'S':LB})
        



@login_required
def view_source(request, submit_id=0):
    from portal.models import Submissions

    a=Submissions.objects.get(submit_id=submit_id)
    return render(request, 'view_source.html', {"i": a.submit_source})

@login_required
def view_mysource(request, submit_id=0):
    from portal.models import Submissions
    from django.contrib.auth.models import User

    a=Submissions.objects.get(submit_id=submit_id)
    return render(request, 'view_mysource.html', {"i": a.submit_source, "name": a.submit_user})



@login_required
def DeleteThisSub(request, submit_id=0):
    from portal.models import Submissions
    a=Announcements.objects.get(submit_id=submit_id)
    a.delete()
    return HttpResponseRedirect('/portal/Submission/')


