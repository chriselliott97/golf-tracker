from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Golfer, Course
from .forms import PracticeForm





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
  practice_form = PracticeForm()
  return render(request, 'golfers/detail.html', { 'golfer': golfer, 'practice_form': practice_form })  

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

def add_practice(request, golfer_id):
  form = PracticeForm(request.POST)
  if form.is_valid():
    new_practice = form.save(commit=False)
    new_practice.golfer_id = golfer_id
    new_practice.save()
  return redirect('golfers_detail', golfer_id=golfer_id)

class CourseCreate(CreateView):
  model = Course
  fields = ['name', 'location']

class CourseList(ListView):
  model = Course

class CourseDetail(DetailView):
  model = Course  

class CourseUpdate(UpdateView):
  model = Course
  fields = ['name', 'color']

class CourseDelete(DeleteView):
  model = Course
  success_url = '/courses/'