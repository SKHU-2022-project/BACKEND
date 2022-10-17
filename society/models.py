from django.db import models

# Create your models here.
#사회 model
class Society(models.Model):
    major = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    merit = models.CharField(max_length=255)
    result = models.CharField(max_length=255)

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