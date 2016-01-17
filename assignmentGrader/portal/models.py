from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    profile_pic = models.ImageField(upload_to='profile_images', blank=True)

    student_score=models.TextField()
    student_submissions=models.TextField()
    #country = models.TextField()

    def __unicode__(self):
        return self.user.username

class Staff(models.Model):
    staff_id=models.TextField(primary_key=True, default="0",editable=False)
    #staff_first_name=models.TextField()
    #staff_last_name=models.TextField()
    #staff_username=models.TextField(max_length()=28)
    ##staff_password=models.CharField(max_length()=50)
    #staff_email=models.TextField()
    #staff_problems=models.TextField()

    def __unicode__(self):
        return self.staff.id

class Problems(models.Model):

    #problem_author=models.ForeignKey('Staff', on_delete=models.CASCADE)
    problem_id=models.TextField(primary_key=True, default="0", editable=False)
    problem_description = models.TextField()
    problem_title = models.CharField(max_length=28)
    test_cases = models.TextField()
    answer_source = models.TextField()
    expected_output=models.TextField()

    def __unicode__(self):
        return self.problem_id

#class Submissions(models.Model):
 #   submit_author=models.ForeignKey('User')
  #  submit_source=models.TextField()
   # submit_output=models.TextField()
    #submit_id=models.TextField()
    #submit_pid=models.TextField()
    #submit_time=models.DateTimeField()
class Announcements(models.Model):
    an_id=models.TextField(primary_key=True, default="0", editable=False)
    an_title=models.CharField(max_length=28)
    an_des=models.TextField()
    an_time=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.an_id


    
