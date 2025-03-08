from django.urls import path
from . import views
urlpatterns = [
    path('register/admin/', views.register_admin, name='register_admin'),
    path('register/employee/', views.register_employee, name='register_employee'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.index, name='index'),
]