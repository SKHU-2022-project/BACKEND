from django.db import models

# Create your models here.
#미컨 model
class MediaContent(models.Model):
    major = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    merit = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    
    def __str__(self):
        return self.major
    
class MediaContentsQuestion(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.number}. {self.question}'
    
class MediaContentsAnswer(models.Model):
    major = models.ForeignKey(MediaContent, on_delete=models.CASCADE)
    question = models.ForeignKey(MediaContentsQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer