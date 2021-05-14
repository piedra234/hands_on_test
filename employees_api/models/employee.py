# Doc

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
