from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models.employee import Employee
from .serializers.employeeSerializer import EmployeeSerializer
from .querysets.employeeQuery import EmployeesQuery
# Create your views here.

class EmployeesAPI (APIView):
    """
    API to gets employees.
    Parameters:
        None: Is used without Url parameters to get all employees.
	Returns: 
		List of employees.
    """
    def get(self, request, *args, **kwargs):
        employees_data = EmployeesQuery()
        employees = employees_data.get_employees()
        employee_serializer = EmployeeSerializer()
        employees_serialized = [employee_serializer.serialize(employee) for employee in employees]
        return Response(employees_serialized)


class EmployeeIdAPI (APIView):
    """
    API to gets employee by id.
    Parameters:
		id: Id from employee.
	Returns: 
		Employee or empty if there is no employee with the id provided.
    """
    def get(self, request, idEmployee, *args, **kwargs):
        employees_data = EmployeesQuery()
        employees = employees_data.get_employee_by_id(idEmployee)         
        employee_serializer = EmployeeSerializer()
        employees_serialized = [employee_serializer.serialize(employee) for employee in employees]
        return Response(employees_serialized)
