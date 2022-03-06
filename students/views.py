from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView
from students.models import StudentDetails
from students.forms import StudentForm
from django.urls import reverse_lazy




# Create your views here.
class AddStudent(CreateView):
    model = StudentDetails
    form_class = StudentForm
    template_name = 'addstudent.html'
    success_url = reverse_lazy('addmark')

class AddMark(ListView):
    model = StudentDetails
    context_object_name = "student"
    template_name = "addmark.html"