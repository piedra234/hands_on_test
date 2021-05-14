from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.EmployeesAPI.as_view(), name="api_employees_id"),
    path('employees/<int:idEmployee>', views.EmployeeIdAPI.as_view(), name="api_employees"),
]
