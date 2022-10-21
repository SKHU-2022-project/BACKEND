from django.db import models

# Create your models here.
#사회 model
class Society(models.Model):
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.major
    
class SocietyQuestion(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class SocietyAnswer(models.Model):
    major = models.ForeignKey(Society, on_delete=models.CASCADE)
    question = models.ForeignKey(SocietyQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer
    
#영어 model
class Society_ENG(models.Model):
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.major
    
class SocietyQuestion_ENG(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class SocietyAnswer_ENG(models.Model):
    major = models.ForeignKey(Society_ENG, on_delete=models.CASCADE)
    question = models.ForeignKey(SocietyQuestion_ENG, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer

#중국어 model
class Society_CN(models.Model):
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.major
    
class SocietyQuestion_CN(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class SocietyAnswer_CN(models.Model):
    major = models.ForeignKey(Society_CN, on_delete=models.CASCADE)
    question = models.ForeignKey(SocietyQuestion_CN, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer

class MediaContentRequirement(models.Model):
    major = models.ForeignKey(Society, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=255)
    ENGrequirement = models.CharField(max_length=255)
    CNrequirement = models.CharField(max_length=255)
    
class MediaContentLearning(models.Model):
    major = models.ForeignKey(Society, on_delete=models.CASCADE)
    learning = models.CharField(max_length=255)
    ENGlearning = models.CharField(max_length=255)
    CNlearning = models.CharField(max_length=255)
    
    def __str__(self):
        return self.major