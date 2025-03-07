from django.shortcuts import render, get_object_or_404, redirect
from .models import Role

# Create your views here.


# List all roles
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role/role_list.html', {'roles': roles})

# Create a new role
def role_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Role.objects.create(name=name)
        return redirect('role-list')
    return render(request, 'role/role_form.html')

# Update an existing role
def role_update(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.name = request.POST.get('name')
        role.save()
        return redirect('role-list')
    return render(request, 'role/role_form.html', {'role': role})

# Delete a role
def role_delete(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('role-list')
    return render(request, 'role/role_confirm_delete.html', {'role': role})
