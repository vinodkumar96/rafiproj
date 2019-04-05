#from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import signup
from .models import signin
from .models import Lovers
import random

def input(request):
    return render(request,'register.html')
def reg(request):
    if request.method == "POST":
        firstname1 = request.POST['fn']
        lastname1 = request.POST['ln']
        dob1 = request.POST['db']
        city1 = request.POST['ct']
        state1 = request.POST['st']
        pincode1 = request.POST['pc']
        about1 = request.POST['ay']
        gender1 = request.POST['gd']
        email1 = request.POST['em']
        phnum1 = request.POST['pn']
        username1 = request.POST['un']
        password1 = request.POST['pd']
        confpass1 = request.POST['cp']
        answer1 = request.POST['ya']
        f = signup(firstname=firstname1,lastname=lastname1,dob=dob1,city=city1,state=state1,pincode=pincode1,
                   about=about1,gender=gender1,email=email1,phnum=phnum1,username=username1,password=password1,
                   confpass=confpass1,answer=answer1)
        f.save()
    return HttpResponse("successfully registerd")
    #else:
        #return render(request, 'regi.html')
def log(request):
    if request.method == "POST":
        email = request.POST['username']
        username = request.POST['username']
        phnum = request.POST['username']
        password = request.POST['password']
        dbuser1 = signup.objects.filter(email =email,password=password)
        dbuser2 = signup.objects.filter(username =username, password=password)
        dbuser3 = signup.objects.filter(phnum =phnum, password=password)
        v = signin(email=email,username=username,phnum=phnum,password=password) #
        v.save()
        if email!="" or username!="" or phnum!="" and password !="": #
            if  dbuser1 or dbuser2 or dbuser3:
                return render(request, "input.html")
                #return HttpResponse("login success")
            else:
                return HttpResponse("login failed")
        else:
            return render(request,"login.html")
    else:

        return render(request,"login.html")
# Create your views here.

#def input(request):
    #return render(request, "h.html")
def feedback(request):
    return render(request, "feedback.html")
def fback (request):
    feedback = request.GET['feedback']
    y=feedback(feedback=feedback)
    y.save()
    return render(request, "feedback.html", {"res": "*Thanking for submitting your Feedback*"})

def image(request):
    return render(request, "image.html")

def terms(request):
    return render(request, "terms.html")
    #return HttpResponse("zzzzzzzzzzzzzzz")
def output(request):
    name = request.POST['t1']
    lovername = request.POST['t2']
    about = request.POST['t3']
    f = Lovers(name=name, lovername=lovername, about=about )
    f.save()
    return render(request,"output.html")
    #return HttpResponse('sucess')

correct=""
def game(request):
    WORDS = ["how","many","want","want","been","else","even",
             "see","doing","would","crazy","way","friends","smile",
             "jerk","them","frown","because","like","friend","might",
             "that","recently","not","old","know","promised","care",
             "most","well","talk","to","be","as","am","me","stake",
             "ignore","why","what","so","and","much","have","acting",
             "but","an","over","everyone","does","little","continue",
             "summary","my","of","mean","ever","without","hate","known",
             "people","towards","everything","let","it"]
    word = random.choice(WORDS)
    #correct=word
    jumble=""
    while word:
        postion=random.randrange(len(word))
        jumble += word[postion]
        word=word[:postion]+word[(postion + 1):]
    return render(request,'game.html',{'word':jumble})
def gues(request):
    WORDS = ["how","many","want","want","been","else","even","see","doing","would",
             "crazy","way","friends","smile","jerk","them","frown","because","like",
             "friend","might","that","recently","not","old","know","promised","care",
             "most","well","talk","to","be","as","am","me","stake","ignore","why",
             "what","so","and","much","have","acting","but","an","over","everyone",
             "does","little","continue","summary","my","of","mean","ever","without",
             "hate","known","people","towards","everything","let","it"]
    guess=request.GET['t4']
    if guess in WORDS:
        return render(request,"game.html",{"out":"*Your Guessing is CORRECT*"})
    else:
        #guess != correct and guess != "":
        return render(request,"game.html",{"out":"Sorry..! Your Guessing is WRONG!"})


