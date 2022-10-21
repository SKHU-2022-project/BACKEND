from django.db import models

# Create your models here.
class ITBoard(models.Model):
    writer = models.CharField(max_length=20)
    date = models.DateTimeField('data published')
    body = models.CharField(max_length=255)
    
    def __str__(self):
        return self.writer
    
class HumanityBoard(models.Model):
    writer = models.CharField(max_length=20)
    date = models.DateTimeField('data published')
    body = models.CharField(max_length=255)
    
    def __str__(self):
        return self.writer


class SocietyBoard(models.Model):
    writer = models.CharField(max_length=20)
    date = models.DateTimeField('data published')
    body = models.CharField(max_length=255)
    
    def __str__(self):
        return self.writer

class MediaContentBoard(models.Model):
    writer = models.CharField(max_length=20)
    date = models.DateTimeField('data published')
    body = models.CharField(max_length=255)
    
    def __str__(self):
        return self.writer