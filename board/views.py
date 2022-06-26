from datetime import date
from django.shortcuts import render, redirect,get_object_or_404
from .models import Board
from django.utils import timezone

# Create your views here.
def boardlist(request):
    posts=Board.objects.filter().order_by('-date')
    return render(request,'board_list.html',{'posts':posts})

def new(request):
    return render(request,'new.html')

def create(request):
    if(request.method=="POST"):
        post=post()
        post.title=request.POST['title']
        # post.name=request.POST['name']
        # post.mbti=request.POST['mbti']
        post.body=request.POST['body']
        post.date=timezone.now()
        post.save()
    return redirect('boardlist')

def detail(request, post_id):
    post_detail=get_object_or_404(Board,pk=post_id)
    return render(request,'detail.html',{'post_detail':post_detail})

def update(request,post_id):
    post_update=Board.objects.get(pk=post_id)
    if request.method=="POST":
        post_update.title=request.POST['title']
        post_update.body=request.POST['body']
        post_update.date=timezone.now()
        post_update.save()
    return redirect('/detail/'+str(post_id), {'post_update':post_update})
    
def delete(request, post_id):
    post_delete = Board.objects.get(pk=post_id)
    post_delete.delete()
    return redirect('boardlist')
        
