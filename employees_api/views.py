from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models.employee import Employee, EmployeesParser
# Create your views here.

class EmployeeAPIView (APIView):
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
        employees_raw = EmployeesParser("http://masglobaltestapi.azurewebsites.net/api/employees")
        if 'id' in request.GET and request.GET["id"] != '':
            employee_id = request.GET["id"]
            employees = employees_raw.get_employee_by_id(employee_id)         
        else:
            employees = employees_raw.get_employees()
        employees_serialized = [employee.serialize() for employee in employees]
        return Response(employees_serialized)