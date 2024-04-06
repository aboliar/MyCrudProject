from django.shortcuts import render,redirect
from demoapp.models import Employee
from demoapp.forms import EmployeeForm

# Create your views here.
def read_view(request):
    employees = Employee.objects.all()
    return render(request,'demoapp/index.html',{'employees':employees})

def create_view(request):
    form = EmployeeForm()
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/emp')
    return render(request,'demoapp/create.html',{'form':form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/emp')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method=='POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/emp')
    return render(request,'demoapp/update.html',{'employee':employee})
