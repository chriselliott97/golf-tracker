from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('golfers/', views.golfers_index, name='golfers_index'),
  path('golfers/<int:golfer_id>/', views.golfers_detail, name='golfers_detail'),
  path('golfers/create/', views.GolferCreate.as_view(), name='golfers_create'),
  path('golfers/<int:pk>/update/', views.GolferUpdate.as_view(), name='golfers_update'),
  path('golfers/<int:pk>/delete/', views.GolferDelete.as_view(), name='golfers_delete'),
  path('golfers/<int:golfer_id>/add_practice/', views.add_practice, name='add_practice'),
  path('courses/create/', views.CourseCreate.as_view(), name='courses_create'),
  path('courses/<int:pk>/', views.CourseDetail.as_view(), name='courses_detail'),
  path('courses/', views.CourseList.as_view(), name='courses_index'),
]