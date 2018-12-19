# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login as auth_login

from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import users1


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signup1(request):
	if request.method=="POST":
		if request.POST.get('name') and request.POST.get("password"):
			post=users1()
			post.name=request.POST.get('name')
			post.password=request.POST.get('password')
			post.save()	
	        return render(request,'signup1.html')
	else:
		return render(request,'signup1.html')


def login1(request):
	if request.method=='GET':
		if request.GET.get('name') and request.GET.get('password'):
			return render(request,'login1.html')