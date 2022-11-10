from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
RANGES = (
  ('5a', '5:00 AM'),
  ('6a', '6:00 AM'),
  ('7a', '7:00 AM'),
  ('8a', '8:00 AM'),
  ('9a', '9:00 AM'),
  ('10a', '10:00 AM'),
  ('11a', '11:00 AM'),
  ('12', '12:00 PM'),
  ('1p', '1:00 PM'),
  ('2p', '2:00 PM'),
  ('3p', '3:00 PM'),
  ('4p', '4:00 PM'),
  ('5p', '5:00 PM'),
  ('6p', '6:00 PM'),
  ('7p', '7:00 PM'),
  ('8p', '8:00 PM'),
  ('9p', '9:00 PM'),
  ('10p', '10:00 PM'),
)
class Course(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  color = models.CharField(max_length=20, default='Green')

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('courses_detail', kwargs={'pk': self.id})


class Golfer(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField('Location (City, State)', max_length=100) 
  experience = models.IntegerField('Experience (Years)')
  age = models.IntegerField()
  courses = models.ManyToManyField(Course)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('golfers_detail', kwargs={'golfer_id': self.id})

  def practiced_for_today(self):
    return self.practice_set.filter(date=date.today()).count() >= len(RANGES)

class Practice(models.Model):
  date = models.DateField('Range date')
  range = models.CharField(
    'Range Time',
    max_length=3,
    choices=RANGES,
    default=RANGES[0][0]
  )

  golfer = models.ForeignKey(Golfer, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_range_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']