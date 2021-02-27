from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.template.context_processors import request
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse
from .forms import sample_form, answer_form
from .grader import inp
from django.contrib.staticfiles.storage import staticfiles_storage
import os
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def graph(request):
    return render(request, 'graph.html')


def signup(request):
    context = {}

    if request.method == 'POST':
        name = request.POST['Form-name']
        username = request.POST['Form-username']
        email = request.POST['Form-email1']
        pass1 = request.POST['Form-pass1']
        pass2 = request.POST['Form-pass2']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('home')

        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return redirect('home')

        else:
            if pass1 == pass2:
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=name)
                user.save()
                user1 = auth.authenticate(username=username,password=pass1)
                if user1 is not None:
                    auth.login(request,user1)
                    return redirect('home')
                


def login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST['Form-usernamelogin']
        passw = request.POST['Form-passlogin1']

        user = auth.authenticate(username=username,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('home')
    else:
        return render(request,'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('/')


def sample_forms(request):
    context = {}
    if request.method == 'POST':
        Sample = sample_form(request.POST, request.FILES)
        context['sample'] = Sample
        if Sample.is_valid():
            Sample.save()
            Name = request.POST['Name']
            Email = request.POST['Email']
            College = request.POST['College']
            Code = request.POST['Code']
            obj = Sample.instance
            sample_answer.objects.filter(sample=obj.sample).update(name=Name, email=Email, college=College, code=Code)
        return redirect('home')
    else:
        Sample = sample_form()
        context['sample'] = Sample
        return render(request, 'sample.html', context)



def student_forms(request):
    context = {}
    if request.method == 'POST':
        Answer = answer_form(request.POST, request.FILES)
        context['answer'] = Answer
        if Answer.is_valid():
            Answer.save()
            Roll = request.POST['Roll']
            Code = request.POST['Code']
            obj = Answer.instance
            student_answer.objects.filter(answer=obj.answer).update(roll=Roll,code=Code)
        return redirect('home')
    else:
        Answer = answer_form()
        context['answer'] = Answer
        return render(request, 'student.html', context)


def check(request):
    score = inp(os.path.join(settings.STATIC_ROOT, 'sample1.txt'),os.path.join(settings.STATIC_ROOT, 'sample2.txt'))
    print(score)
    return redirect('home')