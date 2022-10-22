from distutils.command.upload import upload
from email.policy import default
from enum import unique
from os import setgid
from django.db import models
# from models import Model
# Create your models here.


class DB_teach(models.Model):
    name = models.CharField(max_length=255, unique=False, default='')
    course = models.CharField(max_length=255, unique=False, default='')
    # def __str__(self):
        # return self.name, self.course 

class Tutor(models.Model):
    place_name=models.CharField(max_length=255, default='')
    owner=models.CharField(max_length=255, default='')
    location=models.CharField(max_length=255, default='')
    pic=models.ImageField(null=True, blank=True, upload_to="static/piclocated", unique=True)
    # def __str__(self):
    #     return self.owner, self.place_name, self.location

class Tutor_infor(models.Model):
    tutor = models.ManyToManyField(Tutor)
    nameteach=models.CharField(max_length=255, default='')
    subject=models.CharField(max_length=255, default='')
    expertise=models.CharField(max_length=255, default='')
    experience=models.CharField(max_length=255, default='')
    performance=models.ImageField(null=True, blank=True, upload_to="static/IMG", unique=True)
    VDO=models.FileField(blank=True, upload_to='static/video', unique=True)
    # def __str__(self) :
        # return self.tutor, self.subject, self.expertise, self.experience, self.performance, self.VDO
   