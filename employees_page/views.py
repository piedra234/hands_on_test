from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

from .forms.employeeForm import EmployeeForm
from .services.employeeService import EmployeeService
# Create your views here.

def Employees_view(request, *args, **kargs):
    employee_form = EmployeeForm()
    employee_data = {}
    if request.method == 'POST':
        domain = get_current_site(request)
        employee_service = EmployeeService(str(domain))
        id = request.POST.get('id')
        if id == '':
            employee_data = employee_service.get_employees()
        else:
            employee_data = employee_service.get_employee_by_id(id)
    context = {"employee_form":employee_form,
                "employee_data":employee_data}
    return render(request, "employee/employee.html" , context )