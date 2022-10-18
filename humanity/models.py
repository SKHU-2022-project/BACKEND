from django.db import models

#인문 model
class Humanity(models.Model):
    major = models.CharField(max_length=100)
    
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

#영어 model
class Humanity_ENG(models.Model):
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.major
    
class HumanityQuestion_ENG(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class HumanityAnswer_ENG(models.Model):
    major = models.ForeignKey(Humanity_ENG, on_delete=models.CASCADE)
    question = models.ForeignKey(HumanityQuestion_ENG, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer

#중국어 model
class Humanity_CN(models.Model):
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.major
    
class HumanityQuestion_CN(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class HumanityAnswer_CN(models.Model):
    major = models.ForeignKey(Humanity_CN, on_delete=models.CASCADE)
    question = models.ForeignKey(HumanityQuestion_CN, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer
    
class HumanityBoard(models.Model):
    writer = models.CharField(max_length=20)
    date = models.DateTimeField('data published')
    body = models.CharField(max_length=255)
    
    def __str__(self):
        return self.writer