from django.urls import path
from . import views

urlpatterns = [
    # path('main/',views.Base, name='main_page'),
    path('departments/', views.department_list, name='department-list'),
    path('departments/new/', views.department_create, name='department-create'),
    path('departments/<int:pk>/edit/', views.department_update, name='department-update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department-delete'),
]