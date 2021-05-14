from employees_api.models.employee import Employee
import requests

class EmployeesQuery():
    def __init__(self):
        self.url = "http://masglobaltestapi.azurewebsites.net/api/employees"

    def get_employees(self):
        url = self.url
        employee_json = (requests.get(url)).json()
        employees = [ Employee(employee['id'],
                    employee['name'],
                    employee['contractTypeName'],
                    employee['roleId'],
                    employee['roleName'],
                    employee['roleDescription'],
                    employee['hourlySalary'],
                    employee['monthlySalary']) for employee in employee_json ]
        return employees

    def get_employee_by_id(self, id):
        url = self.url
        employee_json = (requests.get(url)).json()
        employees = [ Employee(employee['id'],
                    employee['name'],
                    employee['contractTypeName'],
                    employee['roleId'],
                    employee['roleName'],
                    employee['roleDescription'],
                    employee['hourlySalary'],
                    employee['monthlySalary'])  for employee in employee_json if employee['id'] == int(id)]
        return employees