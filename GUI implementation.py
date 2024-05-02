import tkinter as tk
from tkinter import messagebox
import pickle

class Employee:
    """Class to represent an employee"""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

class Event:
    """Class to represent an event"""
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers, invoice):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.suppliers = suppliers
        self.invoice = invoice

def add_employee():
    employee = Employee(emp_name_entry.get(), emp_id_entry.get(), emp_dept_entry.get(),
                        emp_title_entry.get(), emp_salary_entry.get(), emp_age_entry.get(),
                        emp_dob_entry.get(), emp_passport_entry.get())
    with open("employees.pkl", "ab") as file:
        pickle.dump(employee, file)
    messagebox.showinfo("Success", "Employee added successfully!")
    clear_employee_fields()

def view_employees():
    try:
        with open("employees.pkl", "rb") as file:
            employees = ""
            while True:
                try:
                    employee = pickle.load(file)
                    employees += f"Employee ID: {employee.employee_id}, Name: {employee.name}, Department: {employee.department}\n"
                except EOFError:
                    break
            if employees:
                messagebox.showinfo("Employees List", employees)
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        messagebox.showerror("Error", "No employees found!")

def clear_employee_fields():
    for entry in [emp_id_entry, emp_name_entry, emp_dept_entry, emp_title_entry, emp_salary_entry, emp_age_entry, emp_dob_entry, emp_passport_entry]:
        entry.delete(0, tk.END)

def add_event():
    entries = event_entries
    event = Event(entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(),
                  entries[4].get(), entries[5].get(), entries[6].get(), entries[7].get(),
                  eval(entries[8].get()), eval(entries[9].get()), entries[10].get())
    with open("events.pkl", "ab") as file:
        pickle.dump(event, file)
    messagebox.showinfo("Success", "Event added successfully!")
    for entry in entries:
        entry.delete(0, tk.END)

def view_events():
    try:
        with open("events.pkl", "rb") as file:
            events = ""
            while True:
                try:
                    event = pickle.load(file)
                    events += f"Event ID: {event.event_id}, Type: {event.event_type}, Date: {event.date}\n"
                except EOFError:
                    break
            if events:
                messagebox.showinfo("Events List", events)
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        messagebox.showerror("Error", "No events found!")

def employee_management():
    emp_window = tk.Toplevel(root)
    emp_window.title("Employee Management")

    global emp_id_entry, emp_name_entry, emp_dept_entry, emp_title_entry, emp_salary_entry, emp_age_entry, emp_dob_entry, emp_passport_entry
    labels = ["Employee ID:", "Name:", "Department:", "Job Title:", "Basic Salary:", "Age:", "Date of Birth:", "Passport Details:"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(emp_window, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(emp_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    emp_id_entry, emp_name_entry, emp_dept_entry, emp_title_entry, emp_salary_entry, emp_age_entry, emp_dob_entry, emp_passport_entry = entries

    tk.Button(emp_window, text="Add Employee", command=add_employee).grid(row=8, column=0, padx=10, pady=5)
    tk.Button(emp_window, text="View Employees", command=view_employees).grid(row=8, column=1, padx=10, pady=5)
    tk.Button(emp_window, text="Clear Fields", command=clear_employee_fields).grid(row=9, column=0, columnspan=2, padx=10, pady=5)

def event_management():
    event_window = tk.Toplevel(root)
    event_window.title("Event Management")

    global event_entries
    labels = ["Event ID", "Event Type", "Theme", "Date", "Time", "Duration", "Venue Address", "Client ID", "Guest List (Python list)", "Suppliers (Python list)", "Invoice"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(event_window, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(event_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    event_entries = entries

    tk.Button(event_window, text="Add Event", command=add_event).grid(row=11, column=0, padx=10, pady=5)
    tk.Button(event_window, text="View All Events", command=view_events).grid(row=11, column=1, padx=10, pady=5)
    tk.Button(event_window, text="Clear Fields", command=lambda: [entry.delete(0, tk.END) for entry in event_entries]).grid(row=12, column=0, columnspan=2, padx=10, pady=5)

def main():
    global root
    root = tk.Tk()
    root.title("Management System")
    tk.Button(root, text="Manage Employees", command=employee_management).pack(side=tk.LEFT, padx=20, pady=20)
    tk.Button(root, text="Manage Events", command=event_management).pack(side=tk.RIGHT, padx=20, pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()
