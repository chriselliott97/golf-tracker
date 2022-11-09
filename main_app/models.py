from django.db import models

# Create your models here.

class Golfer(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100) 
  experience = models.IntegerField()
  age = models.IntegerField()

  def __str__(self):
    return self.name