from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Department

# Create your views here.

# def Base(request):
#     return render(request,'index.html')
# List all departments
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})

# Create a new department
def department_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Department.objects.create(name=name, description=description)
        return redirect('department-list')
    return render(request, 'department/department_form.html')

# Update an existing department
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        department.save()
        return redirect('department-list')
    return render(request, 'department/department_form.html', {'department': department})

# Delete a department
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department-list')
    return render(request, 'department/department_confirm_delete.html', {'department': department})