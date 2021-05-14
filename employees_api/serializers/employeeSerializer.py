from employees_api.models.employee import Employee

class EmployeeSerializer():
   
    def serialize(self, employee):
        employee_serialized = {
                'id' : employee.id,
                'name' : employee.name,
                'contractTypeName' : employee.contract_type_name,
                'roleId' : employee.role_id,
                'roleName' : employee.role_name,
                'roleDescription' : employee.role_description,
                'hourlySalary' : employee.hourly_salary,
                'monthlySalary' : employee.monthly_salary,
                'calculatedAnualSalary' : employee.anual_salary
        }
        return employee_serialized