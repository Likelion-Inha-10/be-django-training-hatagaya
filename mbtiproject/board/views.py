from django.shortcuts import get_object_or_404, redirect, render
from .forms import BoardForm, BoardModelForm,CommentForm
from django.utils import timezone
from account.models import User
from .models import Board
from .models import Comment


# Create your views here.
def boardlist(request):
    posts=Board.objects.filter().order_by('-date')
    return render(request,'board_list.html',{'posts':posts})

def detail(request, board_id):
    # blog_id 번째 블로그 글을 detali.html로 띄어주는 코드
    board_detail = get_object_or_404(Board, pk=board_id)
    #Blog객체를 한 개를 가져올건데 pk값이 blog_id 값인 객체를 가져올것 
    user_id = request.user.id
    
def formcreate(request):
    if request.method=='POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            post=Board()
            user_id=request.user.id
            post.writer=get_object_or_404(User,pk=user_id)
            post.title=form.cleaned_data['title']
            post.body=form.cleaned_data['body']
            post.save()
            return redirect('boardlist')
    else:
        form=BoardForm()
    return render(request,'form_create.html',{'form':form})    


def modelformcreate(request):
    if request.method == 'POST':
        form = BoardModelForm(request.POST)
        if form.is_valid():
            form.save()
            posts = Board.objects.filter().order_by('-date')
            return render(request,'boardlist.html',{'posts': posts})
    else:
        form = BoardModelForm()
    return render(request, 'form_create.html', {'form':form})


def update(request, board_id):
    board=Board.objects.get(pk=board_id)
    if request.method=='POST':
        form=BoardModelForm(request.POST)
        if form.is_valid():
            board.title=form.cleaned_data['title']
            board.body=form.cleaned_data['body']
            board.date=timezone.now()
            board.save()
            return redirect('detail', board_id)
    else:
        post=BoardModelForm(instance=board)
        return render(request,'update.html',{'form':form})

def delete_board(request, board_id):
    board = Board.objects.get(pk = board_id)
    board.delete()
    return redirect('boardlist')

def create_comment(request, board_id):
    filled_form = CommentForm(request.POST)
    
    if filled_form.is_valid():
        comment = Comment()
        comment.comment = filled_form.cleaned_data['comment']
        comment.post = get_object_or_404(Board, pk = board_id)
        comment.post2 = get_object_or_404(User, pk = request.user.id)
        comment.save()
        

def update_comment(request, board_id, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id )
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.comment = form.cleaned_data['comment']
            comment.save()
            return redirect('detail', board_id)
    else:
        form = CommentForm(instance = comment)
        return render(request, 'update_comment.html', {'form' : form})


def delete_comment(request, board_id, comment_id):
    comment = Comment.objects.get(pk = comment_id)
    comment.delete()
    return redirect('detail', board_id)