import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import pickle
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
# Function to add an employee
def add_employee():
    employee_id = emp_id_entry.get()
    name = name_entry.get()
    department = dept_entry.get()
    job_title = job_title_entry.get()
    basic_salary = basic_salary_entry.get()
    age = age_entry.get()
    date_of_birth = dob_entry.get()
    passport_details = passport_entry.get()

    employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)

    # Write employee details to a binary file using Pickle
    with open("employees.pkl", "ab") as file:
        pickle.dump(employee, file)

    messagebox.showinfo("Success", "Employee added successfully!")



# Function to display all employees
def display_employees():
    try:
        # Read employee details from the binary file
        with open("employees.pkl", "rb") as file:
            employee_details = ""
            while True:
                try:
                    employee = pickle.load(file)
                    employee_details += f"Employee ID: {employee.employee_id}\nName: {employee.name}\nDepartment: {employee.department}\nJob Title: {getattr(employee, 'job_title', 'Not available')}\nBasic Salary: {getattr(employee, 'basic_salary', 'Not available')}\nAge: {getattr(employee, 'age', 'Not available')}\nDate of Birth: {getattr(employee, 'date_of_birth', 'Not available')}\nPassport Details: {getattr(employee, 'passport_details', 'Not available')}\n\n"
                except EOFError:
                    break
            if employee_details:
                messagebox.showinfo("Employee Details", employee_details)
            else:
                messagebox.showerror("Error", "No employees found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No employees found!")


# Function to delete an employee
def delete_employee():
    employee_id = delete_entry.get()

    # Read employee details from the binary file
    try:
        with open("employees.pkl", "rb") as file:
            employees = []
            while True:
                try:
                    employee = pickle.load(file)
                    if employee.employee_id != employee_id:
                        employees.append(employee)
                except EOFError:
                    break

        # Write updated employee details back to the file
        with open("employees.pkl", "wb") as file:
            for employee in employees:
                pickle.dump(employee, file)

        messagebox.showinfo("Success", "Employee deleted successfully!")

    except FileNotFoundError:
        messagebox.showerror("Error", "No employees found!")


# Function to clear input fields
def clear_fields():
    emp_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    job_title_entry.delete(0, tk.END)
    basic_salary_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    passport_entry.delete(0, tk.END)
    delete_entry.delete(0, tk.END)
# Main GUI function
def main():
    root = tk.Tk()
    root.title("Management System")

    # Create notebook
    notebook = tk.ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create frames for each entity
    employee_frame = tk.Frame(notebook)
# Add frames to notebook
    notebook.add(employee_frame, text='Employees')
    # Populate each frame with fields and buttons
    populate_employee_frame(employee_frame)
    root.mainloop()
def populate_employee_frame(frame):
    # Labels and entry setup for employee attributes
    labels = ["Employee ID:", "Name:", "Department:", "Job Title:", "Basic Salary:", "Age:", "Date of Birth:", "Passport Details:"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(frame, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    global emp_id_entry, name_entry, dept_entry, job_title_entry, basic_salary_entry, age_entry, dob_entry, passport_entry
    emp_id_entry, name_entry, dept_entry, job_title_entry, basic_salary_entry, age_entry, dob_entry, passport_entry = entries

    # Buttons for employee actions
    tk.Button(frame, text="Add Employee", command=add_employee).grid(row=len(labels), column=0, padx=10, pady=5)
    tk.Button(frame, text="Delete Employee", command=delete_employee).grid(row=len(labels), column=1, padx=10, pady=5)
    tk.Button(frame, text="Display Employees", command=display_employees).grid(row=len(labels) + 1, column=0, padx=10, pady=5)
    tk.Button(frame, text="Clear Fields", command=clear_fields).grid(row=len(labels) + 1, column=1, padx=10, pady=5)
if __name__ == "__main__":
    main()