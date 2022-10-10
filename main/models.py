from tkinter.messagebox import QUESTION
from django.db import models

# Create your models here.
class Question(models.Model): 
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length= 50)

    def __str__(self):
         return f'{self.number}. {self.content}'

class Developer(models.Model):#디벨로퍼에 카운트가 들어가야하는 이유는 사실 딱히 없긴 하지만, 메인에서 보여줄때 연결하기 쉬우니..
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Choice(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(to='main.Question', on_delete=models.CASCADE)
    developer = models.ForeignKey(to='main.developer', on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.content