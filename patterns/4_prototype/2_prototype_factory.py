from copy import deepcopy

class Address:
    def __init__(self, site_no, branch_address, country):
        self.site_no = site_no
        self.branch_address = branch_address
        self.country = country

    def __str__(self):
        return f"No: {self.site_no}\n{self.branch_address}\n{self.country}"

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"The employee named {self.name} is working at {self.address}"
    
        
class EmployeeFactory:

    __main_office_employee = Employee('', Address('', "boleveyard, old chapel road east", "UK"))
    __sub_branch_employee = Employee('', Address('', "vineyard, new chapel road west", "UK"))

    def __create(prototype, employee_name, site_no):
        model = deepcopy(prototype)
        model.name = employee_name
        model.address.site_no = site_no
        return model
    
    @staticmethod
    def new_main_office(employee_name, site_no):
        return EmployeeFactory.__create(EmployeeFactory.__main_office_employee, employee_name, site_no)

    @staticmethod
    def new_sub_branch_office(employee_name, site_no):
        return EmployeeFactory.__create(EmployeeFactory.__sub_branch_employee, employee_name, site_no)
    
john = EmployeeFactory.new_main_office("John", "A wing 103")
print(john)

jane = EmployeeFactory.new_sub_branch_office("Jane", "B wing 220")
print(jane)