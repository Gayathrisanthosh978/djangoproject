from students.models import StudentDetails
from django.forms import ModelForm
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model=StudentDetails
        exclude=('active_status',)
        widgets={
            "Name":forms.TextInput(attrs={"class":"form-control"}),
            "RegisterNumber":forms.NumberInput(attrs={"class":"form-control"}),
            "Email":forms.EmailInput(attrs={"class":"form-control"}),
            "Grade":forms.TextInput(attrs={"class":"form-control"}),

        }