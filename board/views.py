from datetime import date
from django.shortcuts import render, redirect,get_object_or_404
from .models import Board, Comment
from account.models import User
from django.utils import timezone
from .forms import CommentForm

# Create your views here.
def boardlist(request):
    posts=Board.objects.filter().order_by('-date')
    return render(request,'board_list.html',{'posts':posts})

def new(request):
    return render(request,'new.html')

def create(request):
    if(request.method=="POST"):
        post=Board()
        post.title=request.POST['title']
        post.body=request.POST['body']
        post.date=timezone.now()
        post.User_data = get_object_or_404(User, pk=request.user.id)
        post.save()
    return redirect('boardlist')

def detail(request, post_id):
    board_detail=get_object_or_404(Board,pk=post_id)
    return render(request,'detail.html',{'board_detail':board_detail})

def update(request,post_id):
    board_detail=Board.objects.get(pk=post_id)
    if request.method=="POST": 
        board_detail.title=request.POST['title']
        board_detail.body=request.POST['body']
        board_detail.date=timezone.now()
        board_detail.save()
        return redirect('detail/'+str(post_id), {'board_detail':board_detail})
    else:
        return render(request, "updata.html", {'board_detail':board_detail})
    
def delete(request, post_id):
    post_delete = Board.objects.get(pk=post_id)
    post_delete.delete()
    return redirect('boardlist')

def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Board, pk=post_id)
        finished_form.User_data = get_object_or_404(User, pk=request.user.id)
        finished_form.save()
    
    return redirect('detail', post_id)

def delete_comment(request, post_id, comment_id):
    comment_delete = Comment.objects.get(pk=comment_id)
    comment_delete.delete()
    return redirect('detail', post_id)