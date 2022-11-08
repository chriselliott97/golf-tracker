from django.shortcuts import render
from django.http import HttpResponse




class Golfer:
  def __init__(self, name, location, experience, age):
    self.name = name 
    self.location = location 
    self.experience = experience
    self.age = age

golfers = [
  Golfer('Chris', 'Waltham, MA', 7, 25),
  Golfer('Phil', 'Framingham, MA', 10, 26)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def golfers_index(request):
  return render(request, 'golfers/index.html', { 'golfers': golfers })