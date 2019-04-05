# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class signup(models.Model):
    firstname = models.CharField(primary_key=True,max_length=30)
    lastname = models.CharField(max_length=30)
    dob = models.DateField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    about = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    phnum = models.CharField(max_length=10)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    confpass = models.CharField(max_length=15)
    answer = models.CharField(max_length=20)
class signin(models.Model):
    email = models.EmailField(max_length=30)
    username = models.CharField(max_length=15)
    phnum = models.CharField(max_length=10)
    password = models.CharField(max_length=15)

class Lovers(models.Model):
    name=models.CharField(max_length=20)
    lovername=models.CharField(max_length=20)
    about=models.CharField(max_length=60)
class feedback(models.Model):
    fb = models.CharField(max_length=10)

