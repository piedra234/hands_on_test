from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models.employee import Employee
from .serializers.employeeSerializer import EmployeeSerializer
from .querysets.employeeQuery import EmployeesQuery
# Create your views here.

class EmployeesAPIView (APIView):
    """
    API to gets employees
    Parameters:
        *Can be used without Url parameters to get all employees.
		id: Id from employee.
	Returns: 
		List of employees.
        Empty list if there is no employee with the parameter provided.
    """
    def get(self, request, *args, **kwargs):
        employees_data = EmployeesQuery()
        employees = employees_data.get_employees()
        employee_serializer = EmployeeSerializer()
        employees_serialized = [employee_serializer.serialize(employee) for employee in employees]
        return Response(employees_serialized)


class EmployeeIdAPIView (APIView):
    """
    API to gets employees
    Parameters:
        *Can be used without Url parameters to get all employees.
		id: Id from employee.
	Returns: 
		List of employees.
        Empty list if there is no employee with the parameter provided.
    """
    def get(self, request, idEmployee, *args, **kwargs):
        employees_data = EmployeesQuery()
        employees = employees_data.get_employee_by_id(idEmployee)         
        employee_serializer = EmployeeSerializer()
        employees_serialized = [employee_serializer.serialize(employee) for employee in employees]
        return Response(employees_serialized)
