from django.test import TestCase
from employees_api.models.employee import Employee

# Create your tests here.
class EmployeeClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_employee_equals(self):
        print("Method: test_employee_equals.")
        employee = Employee(id= 3, 
                    name= 'Antonio', 
                    contract_type_name= 'HourlySalaryEmployee', 
                    role_id= 1, 
                    role_name= 'Administrator', 
                    role_description= None, 
                    hourly_salary= 120.0, 
                    monthly_salary= 500.0)

        self.assertEquals(employee.anual_salary,172800)

    def test_employee_not_equals(self):
        print("Method: test_employee_not_equals.")
        employee = Employee(id= 3, 
                    name= 'Antonio', 
                    contract_type_name= 'HourlySalaryEmployee', 
                    role_id= 1, 
                    role_name= 'Administrator', 
                    role_description= None, 
                    hourly_salary= 120.0, 
                    monthly_salary= 500.0)

        self.assertEquals(employee.anual_salary,100000)

    def test_exception_contract_type_name(self):
        print("Method: test_exception_contract_type_name.")
        self.assertEquals(employee = Employee(id= 3, 
                    name= 'Antonio', 
                    contract_type_name= 'HourlSalaryEmployee', 
                    role_id= 1, 
                    role_name= 'Administrator', 
                    role_description= None, 
                    hourly_salary= 120.0, 
                    monthly_salary= 500.0)
        )
