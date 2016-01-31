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


class Problems(models.Model):

    #problem_author=models.ForeignKey('Staff', on_delete=models.CASCADE)
    problem_id=models.AutoField(primary_key=True)
    problem_description = models.TextField()
    problem_title = models.CharField(max_length=28)
    test_cases = models.TextField()
    answer_source = models.TextField()
    expected_output=models.TextField()

    def __unicode__(self):
        return self.problem_id

class Submissions(models.Model):
    submit_id=models.AutoField(primary_key=True)
    submit_title=models.TextField()
    submit_user=models.TextField()
    submit_source=models.TextField()
    submit_output=models.TextField()
    submit_verdict=models.TextField()
    submit_score=models.TextField()
    submit_lang=models.TextField()
    submit_pid=models.TextField()
    submit_time=models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.submit_id

class Restrictions(models.Model):
    r_id=models.AutoField(primary_key=True)
    user=models.TextField()
    problemId=models.TextField()
    attempt=models.TextField()


class Announcements(models.Model):
    an_id=models.AutoField(primary_key=True)
    an_title=models.CharField(max_length=28)
    an_des=models.TextField()
    an_time=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.an_id


    
