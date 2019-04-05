# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from .models import signup
from .models import signin
# Register your models here.
class Signupadmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','dob','city','state',
                    'pincode','about','gender','email','phnum',
                    'username','password','confpass','answer']
    list_filter = ['dob']
    class meta:
     model=signup
admin.site.register(signup,Signupadmin)

class Signinadmin(admin.ModelAdmin):
    list_display = ['username','email','password']
    list_filter = ['username']
    class meta:
     model=signin
admin.site.register(signin,Signinadmin)