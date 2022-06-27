from datetime import date
from django.shortcuts import render, redirect,get_object_or_404
from .models import Board
from django.utils import timezone
from .forms import BoardForm

# Create your views here.
def boardlist(request):
    posts=Board.objects.filter().order_by('-pk')
    return render(request,'board_list.html',{'posts':posts})


def formcreate(request):
    if request.method=='POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            post=Board()
            post.title=form.cleaned_data['title']
            post.body=form.cleaned_data['body']
            post.save()
            return redirect('boardlist')
    else:
        form=BoardForm()
    return render(request,'form_create.html',{'form':form})    

def detail(request, board_id):
    board_detail=get_object_or_404(Board,pk=board_id)
    return render(request, 'detail.html', {'board_detail':board_detail})


def update(request, board_id):
    post=Board.objects.get(pk=board_id)
    if request.method=='POST':
        form=BoardForm()
        post.title=request.POST['title']
        post.body=request.POST['body']
        post.date=timezone.now()
        return redirect('/detail/'+str(post.id),{'post':post})
    else:
        post=Board()
        return render(request,'update.html',{'post':post})