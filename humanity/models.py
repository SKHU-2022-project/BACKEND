from django.db import models

#인문 model
class Humanity(models.Model):
    major = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    #image = models.ImageField('image') 학과별 이미지
    
    def __str__(self):
        return self.major
    
class HumanityQuestion(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class HumanityAnswer(models.Model):
    major = models.ForeignKey(Humanity, on_delete=models.CASCADE)
    question = models.ForeignKey(HumanityQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer