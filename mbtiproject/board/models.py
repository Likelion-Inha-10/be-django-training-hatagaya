from django.db import models
from account.models import User

class Board(models.Model):
    title=models.CharField(max_length=100)
    writer=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    
def __str__(self):
    return self.title

class Comment(models.Model):
    comment = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Board, on_delete=models.CASCADE)
    post2 = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    
    def __str__(self):      
        return self.comment  