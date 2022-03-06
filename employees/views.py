from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView,DetailView,UpdateView,DeleteView
from employees.forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from employees.models import EmployeeDetails
from employees.forms import EmployeeForm
from django.urls import reverse_lazy


# Create your views here.
class AddEmp(CreateView):
    model = EmployeeDetails
    form_class = EmployeeForm
    template_name = 'addemp.html'
    success_url = reverse_lazy('emplist')
class Listemp(ListView):
    model = EmployeeDetails
    context_object_name = "employee"
    template_name = 'emplist.html'
class ViewEmp(DetailView):
    model = EmployeeDetails
    context_object_name = 'emp'
    template_name = 'empview.html'
    pk_url_kwarg = 'id'
class EditEmp(UpdateView):
    model = EmployeeDetails
    template_name = "empedit.html"
    form_class = EmployeeForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('emplist')
class DelEmp(DeleteView):
    model = EmployeeDetails
    template_name = 'empdel.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('emplist')
class Registration(View):
    def get(self,request):
        form=UserRegistrationForm()
        context={'form':form}
        return render(request,'registration.html',context)
    def post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user created")
            return render(request,'registration.html')
        else:
            context={'form':form}
            return render(request,'registration.html',context)
class Login(View):
    def get(self,request):
        form=LoginForm
        context={'form':form}
        return render(request,'login.html',context)
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            print(user)
            if user:
                login(request,user)

                return redirect('empadd')

        else:
            context={"form":form}
            return render(request,"login.html",context)