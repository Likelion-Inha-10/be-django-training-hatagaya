from django.shortcuts import redirect, render
from django.contrib import auth
from account.models import User 
from board.models import Board
# Create your views here.

from django.conf import settings
UserModel = settings.AUTH_USER_MODEL

def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        
        user = auth.authenticate(request, username = userid, password = pwd)
       
        if (user is not None):
            auth.login(request, user)
            return redirect('community')
        
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        pwd2 = request.POST['password2']
        name = request.POST['name']

        if pwd == pwd2:
            user = User.objects.create_user(username = userid, password = pwd, name = name)
            auth.login(request, user)
            return render(request, 'MBTI.html')
        
        else:
            return render(request, 'signup.html')
    
    else:
        return render(request, 'signup.html')


def result(request):
    if request.method == 'POST':
        m = str(request.POST['M']) 
        b = str(request.POST['B'])
        t = str(request.POST['T'])
        i = str(request.POST['I'])
        mbti = m+b+t+i
   
        user2 = User.objects.last()
        user2.mbti = mbti 
        user2.save()
    return render(request, 'result.html',{'user2':user2})


def home(request):
    return render(request, 'index.html')
