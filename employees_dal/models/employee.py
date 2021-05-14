# Doc
import requests

class Employee():
    def __init__(self, id, name, contract_type_name, role_id, role_name, role_description, hourly_salary, monthly_salary):
        self.id = id
        self.name = name
        self.contract_type_name = contract_type_name
        self.role_id = role_id
        self.role_name = role_name
        self.role_description = role_description
        self.hourly_salary = hourly_salary
        self.monthly_salary = monthly_salary
        self.anual_salary = self.calculate_anual_salary()

    def calculate_anual_salary(self):
        if self.contract_type_name == 'HourlySalaryEmployee':
            return 120 * self.hourly_salary * 12
        else:
            return self.monthly_salary * 12

    def serialize(self):
        employee = {
                'id' : self.id,
                'name' : self.name,
                'contractTypeName' : self.contract_type_name,
                'roleId' : self.role_id,
                'roleName' : self.role_name,
                'roleDescription' : self.role_description,
                'hourlySalary' : self.hourly_salary,
                'monthlySalary' : self.monthly_salary,
                'calculatedAnualSalary' : self.anual_salary
        }
        return employee


class EmployeesParser():
    def __init__(self, url):
        self.url = url

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
