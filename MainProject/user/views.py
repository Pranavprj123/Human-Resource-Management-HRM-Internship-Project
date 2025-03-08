from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AdminRegistrationForm, EmployeeRegistrationForm, LoginForm

# Create your views here.
def register_admin(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AdminRegistrationForm()
    return render(request, 'user/register_admin.html', {'form': form})

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'user/register_employee.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome {user.role.capitalize()}, {user.username}!')
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html', {'user': request.user})

@login_required
def index(request):
    return render(request, 'index.html', {'user': request.user})