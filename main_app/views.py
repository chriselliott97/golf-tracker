from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Golfer





# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def golfers_index(request):
  golfers = Golfer.objects.all()
  return render(request, 'golfers/index.html', { 'golfers': golfers })

def golfers_detail(request, golfer_id):
  golfer = Golfer.objects.get(id=golfer_id)
  return render(request, 'golfers/detail.html', { 'golfer': golfer })  

class GolferCreate(CreateView):
  model = Golfer
  fields = '__all__'
  success_url = '/golfers/'

class GolferUpdate(UpdateView):
  model = Golfer
  fields = ['location', 'experience', 'age']

class GolferDelete(DeleteView):
  model = Golfer
  success_url = '/golfers/'