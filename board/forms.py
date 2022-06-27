from django import forms
from .models import Board

class BoardForm(forms.Form):
    title=forms.CharField()
    body=forms.CharField(widget=forms.Textarea)
    