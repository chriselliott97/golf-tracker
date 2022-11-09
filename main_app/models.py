from django.db import models
from django.urls import reverse

# Create your models here.
RANGES = (
  ('M', 'Morning'),
  ('N', 'Noon'),
  ('A', 'Afternoon')
)

class Golfer(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField('Location (City, State)', max_length=100) 
  experience = models.IntegerField('Experience (Years)')
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('golfers_detail', kwargs={'golfer_id': self.id})

class Practice(models.Model):
  date = models.DateField('Range date')
  range = models.CharField(
    max_length=1,
    choices=RANGES,
    default=RANGES[0][0]
  )

  golfer = models.ForeignKey(Golfer, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_range_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']