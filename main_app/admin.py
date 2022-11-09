from django.contrib import admin
from .models import Golfer, Practice, Course


# Register your models here.
admin.site.register(Golfer)
admin.site.register(Practice)
admin.site.register(Course)