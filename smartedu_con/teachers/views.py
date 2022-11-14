from django.shortcuts import render
from django.views.generic.list import ListView
from teachers.models import Teachers
from random import random


class TeacherListView(ListView):
    model = Teachers
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    # queryset = Teachers.objects.all()[:1]
    
    # Random List Of Teachers
    def get_queryset(self):
        items = sorted(Teachers.objects.all(), key=lambda x:random())
        return items