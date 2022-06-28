from django import forms
from .models import Board, Comment

class BoardForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget = forms.Textarea)

    
class BoardModelForm(forms.ModelForm):
    class Meta:
        model = Board
        fields=['title','body']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  #Comment라는 모델을 기반으로 입력값을 받을거다
        fields=['comment'] #이 부분만 입력받겠다는 의미
    
