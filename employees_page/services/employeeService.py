import requests

class EmployeeService():
    def __init__(self, domain):
        #self.url = domain + "/api/employees"
        self.url = "http://" + domain  + "/api/employees"

    def get_employees(self):
        url = self.url
        employee_json = (requests.get(url)).json()
        return employee_json

    def get_employee_by_id(self, id):
        url = self.url + '/' + id
        employee_json = (requests.get(url)).json()
        return employee_json