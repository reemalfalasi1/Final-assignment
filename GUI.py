import tkinter as tk
from tkinter import ttk
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


class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id  # Unique identifier for the guest
        self.name = name  # Name of the guest
        self.address = address  # Address of the guest
        self.contact_details = contact_details  # Contact details of the guest


class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id  # Unique identifier for the venue
        self.name = name  # Name of the venue
        self.address = address  # Address of the venue
        self.contact = contact  # Contact information for the venue
        self.min_guests = min_guests  # Minimum number of guests the venue can accommodate
        self.max_guests = max_guests  # Maximum number of guests the venue can accommodate


class Client:
    """Class to represent client"""
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id  # Unique identifier for the client
        self.name = name  # Name of the client
        self.address = address  # Address of the client
        self.contact_details = contact_details  # Contact details of the client
        self.budget = budget  # Budget allocated by the client


class Supplier:
    """class to represent a supplier"""
    def __init__(self, supplier_id, name, address, contact_details, service_type):
        self.supplier_id = supplier_id  # unique identifier for the supplier
        self.name = name  # Name of the supplier
        self.address = address  # Address of the supplier
        self.contact_details = contact_details  # Contact details of the supplier
        self.service_type = service_type  # Type of service provided by the supplier

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


# Function to add a guest
def add_guest():
    guest_id = guest_id_entry.get()
    name = guest_name_entry.get()
    address = guest_address_entry.get()
    contact_details = guest_contact_entry.get()

    guest = Guest(guest_id, name, address, contact_details)

    # Write guest details to a binary file using Pickle
    with open("guests.pkl", "ab") as file:
        pickle.dump(guest, file)

    messagebox.showinfo("Success", "Guest added successfully!")


# Function to delete a guest
def delete_guest():
    guest_id = guest_id_entry.get()

    # Read all guests from the file
    guests = []
    try:
        with open("guests.pkl", "rb") as file:
            while True:
                try:
                    guest = pickle.load(file)
                    if guest.guest_id != guest_id:
                        guests.append(guest)
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showerror("Error", "No guests found!")
        return

    # Write back all guests except the one to be deleted
    with open("guests.pkl", "wb") as file:
        for guest in guests:
            pickle.dump(guest, file)

    messagebox.showinfo("Success", "Guest deleted successfully!")


# Function to modify guest details
def modify_guest():
    guest_id = guest_id_entry.get()
    name = guest_name_entry.get()
    address = guest_address_entry.get()
    contact_details = guest_contact_entry.get()

    # Read all guests from the file
    guests = []
    try:
        with open("guests.pkl", "rb") as file:
            while True:
                try:
                    guest = pickle.load(file)
                    if guest.guest_id == guest_id:
                        # Modify the guest details
                        guest.name = name
                        guest.address = address
                        guest.contact_details = contact_details
                    guests.append(guest)
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showerror("Error", "No guests found!")
        return

    # Write back all guests with modifications
    with open("guests.pkl", "wb") as file:
        for guest in guests:
            pickle.dump(guest, file)

    messagebox.showinfo("Success", "Guest details modified successfully!")




# Function to display guest details
def display_guests():
    try:
        # Read guest details from the binary file
        with open("guests.pkl", "rb") as file:
            guests_details = ""
            while True:
                try:
                    guest = pickle.load(file)
                    guests_details += f"Guest ID: {guest.guest_id}\nName: {guest.name}\nAddress: {guest.address}\nContact Details: {guest.contact_details}\n\n"
                except EOFError:
                    break
        messagebox.showinfo("Guest Details", guests_details)
    except FileNotFoundError:
        messagebox.showerror("Error", "No guests found!")


# Function to add a venue
def add_venue():
    venue_id = venue_id_entry.get()
    name = venue_name_entry.get()
    address = venue_address_entry.get()
    contact = venue_contact_entry.get()
    min_guests = min_guests_entry.get()
    max_guests = max_guests_entry.get()

    venue = Venue(venue_id, name, address, contact, min_guests, max_guests)

    # Write venue details to a binary file using Pickle
    with open("venues.pkl", "ab") as file:
        pickle.dump(venue, file)

    messagebox.showinfo("Success", "Venue added successfully!")

# Function to delete a venue
def delete_venue():
    venue_id = venue_id_entry.get()

    # Read all venues from the file
    venues = []
    try:
        with open("venues.pkl", "rb") as file:
            while True:
                try:
                    venue = pickle.load(file)
                    if venue.venue_id != venue_id:
                        venues.append(venue)
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showerror("Error", "No venues found!")
        return

    # Write back all venues except the one to be deleted
    with open("venues.pkl", "wb") as file:
        for venue in venues:
            pickle.dump(venue, file)

    messagebox.showinfo("Success", "Venue deleted successfully!")


# Function to modify venue details
def modify_venue():
    venue_id = venue_id_entry.get()
    name = venue_name_entry.get()
    address = venue_address_entry.get()
    contact = venue_contact_entry.get()
    min_guests = min_guests_entry.get()
    max_guests = max_guests_entry.get()

    # Read all venues from the file
    venues = []
    try:
        with open("venues.pkl", "rb") as file:
            while True:
                try:
                    venue = pickle.load(file)
                    if venue.venue_id == venue_id:
                        # Modify the venue details
                        venue.name = name
                        venue.address = address
                        venue.contact = contact
                        venue.min_guests = min_guests
                        venue.max_guests = max_guests
                    venues.append(venue)
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showerror("Error", "No venues found!")
        return

    # Write back all venues with modifications
    with open("venues.pkl", "wb") as file:
        for venue in venues:
            pickle.dump(venue, file)

    messagebox.showinfo("Success", "Venue details modified successfully!")




# Function to display venue details
def display_venues():
    try:
        # Read venue details from the binary file
        with open("venues.pkl", "rb") as file:
            venues_details = ""
            while True:
                try:
                    venue = pickle.load(file)
                    venues_details += f"Venue ID: {venue.venue_id}\nName: {venue.name}\nAddress: {venue.address}\nContact: {venue.contact}\nMin Guests: {venue.min_guests}\nMax Guests: {venue.max_guests}\n\n"
                except EOFError:
                    break
        messagebox.showinfo("Venue Details", venues_details)
    except FileNotFoundError:
        messagebox.showerror("Error", "No venues found!")


def display_client_details_by_id():
    client_id = client_id_entry.get()

    # Read all clients from the file
    try:
        with open("clients.pkl", "rb") as file:
            while True:
                try:
                    client = pickle.load(file)
                    if client.client_id == client_id:
                        messagebox.showinfo("Client Details", f"Client ID: {client.client_id}\nName: {client.name}\nAddress: {client.address}\nContact Details: {client.contact_details}\nBudget: {client.budget}")
                        return
                except EOFError:
                    break
        messagebox.showerror("Error", "No client found with the provided ID!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No clients found!")
# Function to add a client
def add_client():
    client_id = client_id_entry.get()
    name = client_name_entry.get()
    address = client_address_entry.get()
    contact_details = client_contact_entry.get()
    budget = client_budget_entry.get()

    client = Client(client_id, name, address, contact_details, budget)

    # Write client details to a binary file using Pickle
    with open("clients.pkl", "ab") as file:
        pickle.dump(client, file)

    messagebox.showinfo("Success", "Client added successfully!")


# Function to delete a client
def delete_client():
    client_id = client_id_entry.get()

    # Read all clients from the file
    clients = []
    try:
        with open("clients.pkl", "rb") as file:
            while True:
                try:
                    client = pickle.load(file)
                    if client.client_id != client_id:
                        clients.append(client)
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showerror("Error", "No clients found!")
        return

    # Write back all clients except the one to be deleted
    with open("clients.pkl", "wb") as file:
        for client in clients:
            pickle.dump(client, file)

    messagebox.showinfo("Success", "Client deleted successfully!")


# Function to modify client details
def modify_client():
    client_id = client_id_entry.get()
    name = client_name_entry.get()
    address = client_address_entry.get()
    contact_details = client_contact_entry.get()
    budget = client_budget_entry.get()

    # Read all clients from the file
    clients = []
    try:
        with open("clients.pkl", "rb") as file:
            while True:
                try:
                    client = pickle.load(file)
                    if client.client_id == client_id:
                        # Modify the client details
                        client.name = name
                        client.address = address
                        client.contact_details = contact_details
                        client.budget = budget
                    clients.append(client)
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showerror("Error", "No clients found!")
        return

    # Write back all clients with modifications
    with open("clients.pkl", "wb") as file:
        for client in clients:
            pickle.dump(client, file)

    messagebox.showinfo("Success", "Client details modified successfully!")


# Function to display client details
def display_clients():
    try:
        # Read client details from the binary file
        with open("clients.pkl", "rb") as file:
            clients_details = ""
            while True:
                try:
                    client = pickle.load(file)
                    clients_details += f"Client ID: {client.client_id}\nName: {client.name}\nAddress: {client.address}\nContact Details: {client.contact_details}\nBudget: {client.budget}\n\n"
                except EOFError:
                    break
        messagebox.showinfo("Client Details", clients_details)
    except FileNotFoundError:
        messagebox.showerror("Error", "No clients found!")


# Function to add a supplier
def add_supplier():
    supplier = Supplier(sup_id_entry.get(), sup_name_entry.get(), sup_address_entry.get(), sup_contact_entry.get())
    with open("suppliers.pkl", "ab") as file:
        pickle.dump(supplier, file)
    messagebox.showinfo("Success", "Supplier added successfully!")
    clear_supplier_fields()


# Function to delete a supplier
def delete_supplier():
    supplier_id = delete_sup_id_entry.get()
    found = False
    updated_suppliers = []
    try:
        with open("suppliers.pkl", "rb") as file:
            while True:
                try:
                    supplier = pickle.load(file)
                    if supplier.supplier_id != supplier_id:
                        updated_suppliers.append(supplier)
                    else:
                        found = True
                except EOFError:
                    break

        if found:
            with open("suppliers.pkl", "wb") as file:
                for sup in updated_suppliers:
                    pickle.dump(sup, file)
            messagebox.showinfo("Success", "Supplier deleted successfully!")
        else:
            messagebox.showerror("Error", "Supplier ID not found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No suppliers found!")


# Function to modify supplier details
def modify_supplier():
    # Function body remains unchanged
    pass
def add_event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers, invoice):
    event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers, invoice)
    with open("events.pkl", "ab") as file:
        pickle.dump(event, file)
    messagebox.showinfo("Success", "Event added successfully!")

def delete_event(event_id):
    updated_events = []
    found = False
    try:
        with open("events.pkl", "rb") as file:
            while True:
                try:
                    event = pickle.load(file)
                    if event.event_id != event_id:
                        updated_events.append(event)
                    else:
                        found = True
                except EOFError:
                    break
        if found:
            with open("events.pkl", "wb") as file:
                for event in updated_events:
                    pickle.dump(event, file)
            messagebox.showinfo("Success", "Event deleted successfully!")
        else:
            messagebox.showerror("Error", "Event ID not found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No events found!")

def modify_event(event_id, new_event_type, new_theme, new_date, new_time, new_duration, new_venue_address, new_client_id, new_guest_list, new_suppliers, new_invoice):
    updated_events = []
    found = False
    try:
        with open("events.pkl", "rb") as file:
            while True:
                try:
                    event = pickle.load(file)
                    if event.event_id == event_id:
                        event.event_type = new_event_type
                        event.theme = new_theme
                        event.date = new_date
                        event.time = new_time
                        event.duration = new_duration
                        event.venue_address = new_venue_address
                        event.client_id = new_client_id
                        event.guest_list = new_guest_list
                        event.suppliers = new_suppliers
                        event.invoice = new_invoice
                        found = True
                    updated_events.append(event)
                except EOFError:
                    break
        if found:
            with open("events.pkl", "wb") as file:
                for event in updated_events:
                    pickle.dump(event, file)
            messagebox.showinfo("Success", "Event modified successfully!")
        else:
            messagebox.showerror("Error", "Event not found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No events found!")

def display_events():
    try:
        with open("events.pkl", "rb") as file:
            events_details = ""
            while True:
                try:
                    event = pickle.load(file)
                    events_details += (f"Event ID: {event.event_id}\nType: {event.event_type}\nTheme: {event.theme}\n"
                                       f"Date: {event.date}\nTime: {event.time}\nDuration: {event.duration}\n"
                                       f"Venue Address: {event.venue_address}\nClient ID: {event.client_id}\n"
                                       f"Guest List: {event.guest_list}\nSuppliers: {event.suppliers}\nInvoice: {event.invoice}\n\n")
                except EOFError:
                    break
            if events_details:
                messagebox.showinfo("Event Details", events_details)
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        messagebox.showerror("Error", "No events found!")

def clear_event_fields(entries):
    for entry in entries:
        entry.delete(0, tk.END)

# Function to display supplier details
def display_suppliers():
    try:
        with open("suppliers.pkl", "rb") as file:
            suppliers = ""
            while True:
                try:
                    supplier = pickle.load(file)
                    suppliers += f"Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Address: {supplier.address}\n"
                except EOFError:
                    break
            if suppliers:
                messagebox.showinfo("Suppliers List", suppliers)
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        messagebox.showerror("Error", "No suppliers found!")


# Function to display details of a client given ID number
def display_client_details_by_id():
    client_id = client_id_entry.get()
    found = False
    try:
        with open("clients.pkl", "rb") as file:
            while True:
                try:
                    client = pickle.load(file)
                    if client.client_id == client_id:
                        messagebox.showinfo("Client Details",
                                            f"Client ID: {client.client_id}, Name: {client.name}, Address: {client.address}")
                        found = True
                        break
                except EOFError:
                    break
        if not found:
            messagebox.showerror("Error", "Client not found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No clients found!")



# Function to display details of a supplier given ID number
def display_supplier_details_by_id():
    supplier_id = supplier_id_entry.get()
    found = False
    try:
        with open("suppliers.pkl", "rb") as file:
            while True:
                try:
                    supplier = pickle.load(file)
                    if supplier.supplier_id == supplier_id:
                        messagebox.showinfo("Supplier Details",
                                            f"Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Address: {supplier.address}")
                        found = True
                        break
                except EOFError:
                    break
        if not found:
            messagebox.showerror("Error", "Supplier not found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No suppliers found!")

# Function to display details of a guest given ID number
def display_guest_details_by_id():
    guest_id = guest_id_entry.get()
    found = False
    try:
        with open("guests.pkl", "rb") as file:
            while True:
                try:
                    guest = pickle.load(file)
                    if guest.guest_id == guest_id:
                        messagebox.showinfo("Guest Details",
                                            f"Guest ID: {guest.guest_id}, Name: {guest.name}, Address: {guest.address}")
                        found = True
                        break
                except EOFError:
                    break
        if not found:
            messagebox.showerror("Error", "Guest not found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No guests found!")


# Function to display details of a venue given ID number
def display_venue_details_by_id():
    venue_id = venue_id_entry.get()
    found = False
    try:
        with open("venues.pkl", "rb") as file:
            while True:
                try:
                    venue = pickle.load(file)
                    if venue.venue_id == venue_id:
                        messagebox.showinfo("Venue Details",
                                            f"Venue ID: {venue.venue_id}, Name: {venue.name}, Address: {venue.address}")
                        found = True
                        break
                except EOFError:
                    break
        if not found:
            messagebox.showerror("Error", "Venue not found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No venues found!")



# Main GUI function
def main():
    root = tk.Tk()
    root.title("Management System")

    # Create notebook
    notebook = tk.ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create frames for each entity
    employee_frame = tk.Frame(notebook)
    guest_frame = tk.Frame(notebook)
    venue_frame = tk.Frame(notebook)
    client_frame = tk.Frame(notebook)
    supplier_frame = tk.Frame(notebook)
    event_frame = tk.Frame(notebook)

    # Add frames to notebook
    notebook.add(employee_frame, text='Employees')
    notebook.add(guest_frame, text='Guests')
    notebook.add(venue_frame, text='Venues')
    notebook.add(client_frame, text='Clients')
    notebook.add(supplier_frame, text='Suppliers')
    notebook.add(event_frame, text='Events')


    # Populate each frame with fields and buttons
    populate_employee_frame(employee_frame)
    populate_guest_frame(guest_frame)
    populate_venue_frame(venue_frame)
    populate_client_frame(client_frame)
    populate_supplier_frame(supplier_frame)
    populate_event_frame(event_frame)

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

def populate_guest_frame(frame):
    # Labels and entry setup for guest attributes
    labels = ["Guest ID:", "Name:", "Address:", "Contact Details:"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(frame, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    global guest_id_entry, guest_name_entry, guest_address_entry, guest_contact_entry
    guest_id_entry, guest_name_entry, guest_address_entry, guest_contact_entry = entries

    # Buttons for guest actions
    tk.Button(frame, text="Add Guest", command=add_guest).grid(row=len(labels), column=0, padx=10, pady=5)
    tk.Button(frame, text="Delete Guest", command=delete_guest).grid(row=len(labels), column=1, padx=10, pady=5)
    tk.Button(frame, text="Display Guests", command=display_guests).grid(row=len(labels) + 1, column=0, padx=10, pady=5)
    tk.Button(frame, text="Clear Fields", command=lambda: [entry.delete(0) for entry in entries]).grid(row=len(labels) + 1, column=1, padx=10, pady=5)

def populate_venue_frame(frame):
    # Labels and entry setup for venue attributes
    labels = ["Venue ID:", "Name:", "Address:", "Contact:", "Min Guests:", "Max Guests:"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(frame, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    global venue_id_entry, venue_name_entry, venue_address_entry, venue_contact_entry, min_guests_entry, max_guests_entry
    venue_id_entry, venue_name_entry, venue_address_entry, venue_contact_entry, min_guests_entry, max_guests_entry = entries

    # Buttons for venue actions
    tk.Button(frame, text="Add Venue", command=add_venue).grid(row=len(labels), column=0, padx=10, pady=5)
    tk.Button(frame, text="Delete Venue", command=delete_venue).grid(row=len(labels), column=1, padx=10, pady=5)
    tk.Button(frame, text="Display Venues", command=display_venues).grid(row=len(labels) + 1, column=0, padx=10, pady=5)
    tk.Button(frame, text="Clear Fields", command=lambda: [entry.delete(0) for entry in entries]).grid(row=len(labels) + 1, column=1, padx=10, pady=5)

def populate_client_frame(frame):
    # Labels and entry setup for client attributes
    labels = ["Client ID:", "Name:", "Address:", "Contact Details:", "Budget:"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(frame, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    global client_id_entry, client_name_entry, client_address_entry, client_contact_entry, client_budget_entry
    client_id_entry, client_name_entry, client_address_entry, client_contact_entry, client_budget_entry = entries

    # Buttons for client actions
    tk.Button(frame, text="Add Client", command=add_client).grid(row=len(labels), column=0, padx=10, pady=5)
    tk.Button(frame, text="Delete Client", command=delete_client).grid(row=len(labels), column=1, padx=10, pady=5)
    tk.Button(frame, text="Display Clients", command=display_clients).grid(row=len(labels) + 1, column=0, padx=10, pady=5)
    tk.Button(frame, text="Clear Fields", command=lambda: [entry.delete(0) for entry in entries]).grid(row=len(labels) + 1, column=1, padx=10, pady=5)
def populate_supplier_frame(frame):
    # Labels and entry setup for supplier attributes
    labels = ["Supplier ID:", "Name:", "Address:", "Contact Details:", "Service Type:"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(frame, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    global sup_id_entry, sup_name_entry, sup_address_entry, sup_contact_entry, service_type_entry
    sup_id_entry, sup_name_entry, sup_address_entry, sup_contact_entry, service_type_entry = entries

    # Buttons for supplier actions
    tk.Button(frame, text="Add Supplier", command=add_supplier).grid(row=len(labels), column=0, padx=10, pady=5)
    tk.Button(frame, text="Delete Supplier", command=delete_supplier).grid(row=len(labels), column=1, padx=10, pady=5)
    tk.Button(frame, text="Modify Supplier", command=modify_supplier).grid(row=len(labels) + 1, column=0, padx=10, pady=5)
    tk.Button(frame, text="Display Suppliers", command=display_suppliers).grid(row=len(labels) + 1, column=1, padx=10, pady=5)
    tk.Button(frame, text="Clear Fields", command=lambda: [entry.delete(0, tk.END) for entry in entries]).grid(row=len(labels) + 2, column=0, columnspan=2, padx=10, pady=5)


def populate_event_frame(frame):
    # Labels and entry setup for event attributes
    labels = [
        "Event ID:", "Event Type:", "Theme:", "Date:", "Time:",
        "Duration:", "Venue Address:", "Client ID:", "Guest List:",
        "Suppliers:", "Invoice:"
    ]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(frame, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    global event_id_entry, event_type_entry, theme_entry, date_entry, time_entry, \
        duration_entry, venue_address_entry, client_id_entry, guest_list_entry, \
        suppliers_entry, invoice_entry
    (event_id_entry, event_type_entry, theme_entry, date_entry, time_entry,
     duration_entry, venue_address_entry, client_id_entry, guest_list_entry,
     suppliers_entry, invoice_entry) = entries

    # Buttons for event actions
    tk.Button(frame, text="Add Event", command=lambda: add_event(
        event_id_entry.get(), event_type_entry.get(), theme_entry.get(), date_entry.get(),
        time_entry.get(), duration_entry.get(), venue_address_entry.get(),
        client_id_entry.get(), guest_list_entry.get(), suppliers_entry.get(), invoice_entry.get()
    )).grid(row=len(labels), column=0, padx=10, pady=5)

    tk.Button(frame, text="Delete Event", command=lambda: delete_event(event_id_entry.get())).grid(row=len(labels),
                                                                                                   column=1, padx=10,
                                                                                                   pady=5)

    tk.Button(frame, text="Modify Event", command=lambda: modify_event(
        event_id_entry.get(), event_type_entry.get(), theme_entry.get(), date_entry.get(),
        time_entry.get(), duration_entry.get(), venue_address_entry.get(),
        client_id_entry.get(), guest_list_entry.get(), suppliers_entry.get(), invoice_entry.get()
    )).grid(row=len(labels) + 1, column=0, padx=10, pady=5)

    tk.Button(frame, text="Display Events", command=display_events).grid(row=len(labels) + 1, column=1, padx=10, pady=5)

    tk.Button(frame, text="Clear Fields", command=lambda: [entry.delete(0, tk.END) for entry in entries]).grid(
        row=len(labels) + 2, column=0, columnspan=2, padx=10, pady=5)


if __name__ == "__main__":
    main()