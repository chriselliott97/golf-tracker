from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .models import Golfer, Course
from .forms import PracticeForm





# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def golfers_index(request):
  golfers = Golfer.objects.filter(user=request.user)
  return render(request, 'golfers/index.html', { 'golfers': golfers })

@login_required
def golfers_detail(request, golfer_id):
  golfer = Golfer.objects.get(id=golfer_id)
  courses_golfer_doesnt_have = Course.objects.exclude(id__in = golfer.courses.all().values_list('id'))
  practice_form = PracticeForm()
  return render(request, 'golfers/detail.html', { 'golfer': golfer, 'practice_form': practice_form, 'courses': courses_golfer_doesnt_have })  

class GolferCreate(LoginRequiredMixin, CreateView):
  model = Golfer
  fields = ['name', 'age', 'location', 'experience']
  success_url = '/golfers/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GolferUpdate(LoginRequiredMixin, UpdateView):
  model = Golfer
  fields = ['location', 'experience', 'age']

class GolferDelete(LoginRequiredMixin, DeleteView):
  model = Golfer
  success_url = '/golfers/'

@login_required
def add_practice(request, golfer_id):
  form = PracticeForm(request.POST)
  if form.is_valid():
    new_practice = form.save(commit=False)
    new_practice.golfer_id = golfer_id
    new_practice.save()
  return redirect('golfers_detail', golfer_id=golfer_id)

class CourseCreate(LoginRequiredMixin, CreateView):
  model = Course
  fields = ['name', 'location']

class CourseList(LoginRequiredMixin, ListView):
  model = Course

class CourseDetail(LoginRequiredMixin, DetailView):
  model = Course  

class CourseUpdate(LoginRequiredMixin, UpdateView):
  model = Course
  fields = ['name', 'location']

class CourseDelete(LoginRequiredMixin, DeleteView):
  model = Course
  success_url = '/courses/'

@login_required
def assoc_course(request, golfer_id, course_id):
  Golfer.objects.get(id=golfer_id).courses.add(course_id)
  return redirect('golfers_detail', golfer_id=golfer_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('golfers_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)