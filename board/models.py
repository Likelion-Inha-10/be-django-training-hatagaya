from sys import maxsize
from django.db import models

# Create your models here.
class Board(models.Model):
    title=models.CharField(max_length=200)
    # name=models.CharField(max_length=10)
    # mbti=models.CharField(max_length=4)
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    
def __str__(self):
    return self.title