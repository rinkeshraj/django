from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import requests
import os
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def ABOUT(request):
    return render(request,'ABOUT.html')


# @login_required(login_url='login') 
def home(request):
    
    return render(request,'pre.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username OR Password is incorrect ') 
               
    context = {}
    return render(request,'login.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+user)
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')   

from subprocess import run,PIPE
import sys
def button(request):
    return render(request,'pre.html')
def output(request):
    data=requests.get("")
    print(data.text)
    data=data.text
    return render(request,'pre.html',{'data':data})  

def external(request):
    team1=request.POST.get('team1')
    team2=request.POST.get('team2')
    
    out=run(sys.executable,['//usr//bin//minipro//hii.py',team1,team2],shell=False,stdout=PIPE)
    print(out)
    return render(request,'pre.html',{'data1':out.stdout})