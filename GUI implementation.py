import tkinter as tk
from tkinter import messagebox
import pickle


class Employee:
    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department


# Function to add an employee
def add_employee():
    employee_id = emp_id_entry.get()
    name = name_entry.get()
    department = dept_entry.get()

    employee = Employee(employee_id, name, department)

    # Write employee details to a binary file using Pickle
    with open("employees.pkl", "ab") as file:
        pickle.dump(employee, file)

    messagebox.showinfo("Success", "Employee added successfully!")


# Function to display all employees
def display_employees():
    try:
        # Read employee details from the binary file
        with open("employees.pkl", "rb") as file:
            while True:
                try:
                    employee = pickle.load(file)
                    print("Employee ID:", employee.employee_id)
                    print("Name:", employee.name)
                    print("Department:", employee.department)
                    print()
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showerror("Error", "No employees found!")


# Function to clear input fields
def clear_fields():
    emp_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)


# Main GUI function
def main():
    global emp_id_entry, name_entry, dept_entry

    root = tk.Tk()
    root.title("Employee Management System")

    # Labels
    tk.Label(root, text="Employee ID:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(root, text="Department:").grid(row=2, column=0, padx=10, pady=5)

    # Entry fields
    emp_id_entry = tk.Entry(root)
    name_entry = tk.Entry(root)
    dept_entry = tk.Entry(root)

    emp_id_entry.grid(row=0, column=1, padx=10, pady=5)
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    dept_entry.grid(row=2, column=1, padx=10, pady=5)

    # Buttons
    tk.Button(root, text="Add Employee", command=add_employee).grid(row=3, column=0, padx=10, pady=5)
    tk.Button(root, text="Display Employees", command=display_employees).grid(row=3, column=1, padx=10, pady=5)
    tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
