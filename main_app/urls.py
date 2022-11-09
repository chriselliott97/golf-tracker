from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('golfers/', views.golfers_index, name='golfers_index'),
  path('golfers/<int:golfer_id>/', views.golfers_detail, name='golfers_detail'),
  path('golfers/create/', views.GolferCreate.as_view(), name='golfers_create'),
]