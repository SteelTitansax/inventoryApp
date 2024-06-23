from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):

    return render(request,'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        try:
         if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],password = request.POST['password1'])
            user.save()
            login(request,user)
            return redirect('tasks')
        except IntegrityError:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'User already exists'
            })

    return render(request, 'signup.html', {
        'form': UserCreationForm,
        'error': 'Password do not match'
    })


@login_required
def signout(request):
    logout(request)
    return redirect(home)

def signin(request):
    if request.method == 'GET':

        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password = request.POST['password']
        )
        if user is None :
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error' : 'Username or passowrd is incorrect'
            })
        else:
            login(request,user)
            #return redirect('tasks')

