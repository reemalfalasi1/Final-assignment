class Employee:
    """Class to represent an employee"""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        #constructor to initialize the Employee object with provided attributes
        self.name = name  #employee's name
        self.employee_id = employee_id  #employee's ID
        self.department = department  #department where the employee works
        self.job_title = job_title  #job title of the employee
        self.basic_salary = basic_salary  #basic salary of the employee
        self.age = age  # Age of the employee
        self.date_of_birth = date_of_birth #date of birth of the employee
        self.passport_details = passport_details#passport details of the employee

    # Getters and Setters for each attribute
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_job_title(self):
        return self.job_title

    def set_job_title(self, job_title):
        self.job_title = job_title

    def get_basic_salary(self):
        return self.basic_salary

    def set_basic_salary(self, basic_salary):
        self.basic_salary = basic_salary

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def get_passport_details(self):
        return self.passport_details

    def set_passport_details(self, passport_details):
        self.passport_details = passport_details
