from django.db import models

# Create your models here.
#미컨 model
class MediaContent(models.Model):
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.major
    
class MediaContentQuestion(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.number}. {self.question}'
    
class MediaContentAnswer(models.Model):
    major = models.ForeignKey(MediaContent, on_delete=models.CASCADE)
    question = models.ForeignKey(MediaContentQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer
    
#영어 model
class MediaContent_ENG(models.Model):
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.major
    
class MediaContentQuestion_ENG(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class MediaContentAnswer_ENG(models.Model):
    major = models.ForeignKey(MediaContent_ENG, on_delete=models.CASCADE)
    question = models.ForeignKey(MediaContentQuestion_ENG, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer

#중국어 model
class MediaContent_CN(models.Model):
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.major
    
class MediaContentQuestion_CN(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class MediaContentAnswer_CN(models.Model):
    major = models.ForeignKey(MediaContent_CN, on_delete=models.CASCADE)
    question = models.ForeignKey(MediaContentQuestion_CN, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer
    
class MediaContentRequirement(models.Model):
    major = models.ForeignKey(MediaContent, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=255)
    ENGrequirement = models.CharField(max_length=255)
    CNrequirement = models.CharField(max_length=255)
    
class MediaContentLearning(models.Model):
    major = models.ForeignKey(MediaContent, on_delete=models.CASCADE)
    learning = models.CharField(max_length=255)
    ENGlearning = models.CharField(max_length=255)
    CNlearning = models.CharField(max_length=255)
    
    def __str__(self):
        return self.major
    
class MediaContentRequirement(models.Model):
    major = models.ForeignKey(MediaContent, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=255)
    ENGrequirement = models.CharField(max_length=255)
    CNrequirement = models.CharField(max_length=255)
    
    def __str__(self):
        return self.requirement
    
class MediaContentLearning(models.Model):
    major = models.ForeignKey(MediaContent, on_delete=models.CASCADE)
    learning = models.CharField(max_length=255)
    ENGlearning = models.CharField(max_length=255)
    CNlearning = models.CharField(max_length=255)
    
    def __str__(self):
        return self.learning