from sys import maxsize
from turtle import ondrag
from django.db import models
from tkinter import CASCADE
from account.models import User

# Create your models here.
class Board(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    User_data=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Board, on_delete=models.CASCADE)
    User_data = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    