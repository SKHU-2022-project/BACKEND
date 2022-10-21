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

class HumanityRequirement(models.Model):
    major = models.ForeignKey(Humanity, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=255)
    ENGrequirement = models.CharField(max_length=255)
    CNrequirement = models.CharField(max_length=255)
    
class HumanityLearning(models.Model):
    major = models.ForeignKey(Humanity, on_delete=models.CASCADE)
    learning = models.CharField(max_length=255)
    ENGlearning = models.CharField(max_length=255)
    CNlearning = models.CharField(max_length=255)
    
    def __str__(self):
        return self.major