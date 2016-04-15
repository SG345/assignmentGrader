"""assignmentGrader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

      #auth
      ('^$', 'portal.views.homepage'),
      ('^home/$', 'portal.views.homepage'),
      ('^portal/register/$','portal.views.register'),
      ('^portal/registerme/$','portal.views.show_reg_form'), 
      ('^portal/login/$', 'portal.views.user_login'),
      ('^portal/login/landing$', 'portal.views.show_problems'),
      ('^portal/registerme/portal/register/home', 'portal.views.homepage'),
      ('^portal/logoutme/$', 'portal.views.logout_me'),
      ('^portal/login/logoutme/$', 'portal.views.logout_me'),
      ('^home/logoutme$', 'portal.views.logout_me'),
      ('logoutme/', 'portal.views.logout_me'),

    #announcement
      ('^portal/an$', 'portal.views.show_an'),
      ('^portal/an_staff$', 'portal.views.show_an_staff'),
      ('^portal/add_an/$', 'portal.views.add_an'),
      (r'^portal/delete_an/(?P<an_id>\d+)/$', 'portal.views.DeleteThisAn'),
    #staff
      ('^portal/staff_home/$', 'portal.views.show_staff'),
      ('^portal/add_prob$', 'portal.views.add_problem'),
      ('^portal/add_problem$', 'portal.views.add_prob_form'),
      ('^portal/psuccess/$', 'portal.views.psu'),
      ('^portal/edit_problem/$', 'portal.views.edit_problem'),
      ('^portal/editted_prob/$', 'portal.views.add_editted_prob'),
     (r'^portal/delete/(?P<pid>\d+)/$', 'portal.views.DeleteThisProb'),
    #student
      (r'^problem/(?P<problem_id>\d+)/$', 'portal.views.show_ind_problem'),
      (r'^submit/(?P<problem_id>\d+)/$', 'portal.views.submit_status'),
      ('^portal/rank/$', 'portal.views.rankBoard'),
    #Submission
      ('^portal/Submission/$', 'portal.views.submission_history'),

      (r'^viewsource/(?P<submit_id>\d+)/$', 'portal.views.view_source'),

      (r'^view_mysource/(?P<submit_id>\d+)/$', 'portal.views.view_mysource'),

      (r'^tinymce/', include('tinymce.urls')),


)


#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^register/$', register,name='register'),
#]
