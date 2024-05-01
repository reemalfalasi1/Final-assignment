import tkinter as tk
from tkinter import messagebox
import pickle


class Employee:
    """Class to represent an employee"""
    def __init__(self, name, employee_id, department, job_title=None, basic_salary=None, age=None, date_of_birth=None, passport_details=None):
        # Constructor to initialize the Employee object with provided attributes
        self.name = name  # Employee's name
        self.employee_id = employee_id  # Employee's ID
        self.department = department  # Department where the employee works
        self.job_title = job_title  # Job title of the employee
        self.basic_salary = basic_salary  # Basic salary of the employee
        self.age = age  # Age of the employee
        self.date_of_birth = date_of_birth  # Date of birth of the employee
        self.passport_details = passport_details  # Passport details of the employee


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


# Function to handle Employee management window
def employee_management():
    employee_window = tk.Toplevel(root)
    employee_window.title("Employee Management")

    # Labels
    tk.Label(employee_window, text="Employee ID:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(employee_window, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(employee_window, text="Department:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(employee_window, text="Job Title:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(employee_window, text="Basic Salary:").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(employee_window, text="Age:").grid(row=5, column=0, padx=10, pady=5)
    tk.Label(employee_window, text="Date of Birth:").grid(row=6, column=0, padx=10, pady=5)
    tk.Label(employee_window, text="Passport Details:").grid(row=7, column=0, padx=10, pady=5)
    tk.Label(employee_window, text="Employee ID to Delete:").grid(row=8, column=0, padx=10, pady=5)

    # Entry fields
    global emp_id_entry, name_entry, dept_entry, job_title_entry, basic_salary_entry, age_entry, dob_entry, passport_entry, delete_entry
    emp_id_entry = tk.Entry(employee_window)
    name_entry = tk.Entry(employee_window)
    dept_entry = tk.Entry(employee_window)
    job_title_entry = tk.Entry(employee_window)
    basic_salary_entry = tk.Entry(employee_window)
    age_entry = tk.Entry(employee_window)
    dob_entry = tk.Entry(employee_window)
    passport_entry = tk.Entry(employee_window)
    delete_entry = tk.Entry(employee_window)

    emp_id_entry.grid(row=0, column=1, padx=10, pady=5)
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    dept_entry.grid(row=2, column=1, padx=10, pady=5)
    job_title_entry.grid(row=3, column=1, padx=10, pady=5)
    basic_salary_entry.grid(row=4, column=1, padx=10, pady=5)
    age_entry.grid(row=5, column=1, padx=10, pady=5)
    dob_entry.grid(row=6, column=1, padx=10, pady=5)
    passport_entry.grid(row=7, column=1, padx=10, pady=5)
    delete_entry.grid(row=8, column=1, padx=10, pady=5)

    # Buttons
    tk.Button(employee_window, text="Add Employee", command=add_employee).grid(row=9, column=0, padx=10, pady=5)
    tk.Button(employee_window, text="Display Employees", command=display_employees).grid(row=9, column=1, padx=10, pady=5)
    tk.Button(employee_window, text="Delete Employee", command=delete_employee).grid(row=10, column=0, padx=10, pady=5)
    tk.Button(employee_window, text="Clear Fields", command=clear_fields).grid(row=11, column=0, columnspan=2, padx=10, pady=5)


# Main GUI function
def main():
    global root

    root = tk.Tk()
    root.title("Employee Management System")

    # Button to open Employee management window
    tk.Button(root, text="Employee", command=employee_management).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()



