from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.role_list, name='role-list'),
    path('roles/new/', views.role_create, name='role-create'),
    path('roles/<int:pk>/edit/', views.role_update, name='role-update'),
    path('roles/<int:pk>/delete/', views.role_delete, name='role-delete'),
]
