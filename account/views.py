from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from .models import UserManager, User

from account.models import UserManager

def login(request):
    if(request.method == 'POST'):
        userid = request.POST['id']
        pwd = request.POST['password']

        user = auth.authenticate(id=userid, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('/') # MBTI 게시판으로 이동
        else:
            return redirect('login') # 정보 없으면 다시 로그인으로 돌아감

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login') # 로그인 화면으로 돌아가기 

def signup(request):
    if(request.method == 'POST'):
        if request.POST['password1'] == request.POST['password2']:
            MBTI = request.POST['IorE'] + request.POST['SorN'] + request.POST['TorF'] + request.POST['JorP']
            user = User.objects.create_user(
                id = request.POST['id'],
                name = request.POST['name'],
                MBTI = MBTI,
                password = request.POST['password1']
            )
            auth.login(request, user)

            return redirect('/') # 게시판으로 이동
        return render(request, 'signup.html')
    return render(request, 'signup.html')
