from django.urls import path
from . import views

urlpatterns = [
    path('Employee', views.EmployeesAPIView.as_view(), name="employees_id"),
    path('Employee/<int:idEmployee>', views.EmployeeIdAPIView.as_view(), name="employees"),
]
