from django.shortcuts import render
from django.http import HttpResponse
from students.models import Students
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .forms import StudentForm
# Create your views here.

class StudentList(ListView):
    model = Students
    context_object_name = 'students'

class AddStudent(CreateView):
    model = Students
    form_class = StudentForm
    success_url = reverse_lazy('stu-list')







