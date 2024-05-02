class Event:
    """Class to represent an event"""
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers, invoice):
        self.event_id = event_id  #unique identifier for the event
        self.event_type = event_type  #type of event (e.g., wedding, birthday, corporate)
        self.theme = theme  #theme of the event
        self.date = date  #tate of the event
        self.time = time  #time of the event
        self.duration = duration  #duration of the event
        self.venue_address = venue_address  #address of the venue
        self.client_id = client_id  # ID of the client organizing the event
        self.guest_list = guest_list#List of Guest objects attending the event
        self.suppliers = suppliers # List of Supplier objects providing services for the event
        self.invoice = invoice #Invoice details for the event

    # Getter method for event ID
    def get_event_id(self):
        return self.event_id

    # Setter method for event ID
    def set_event_id(self, event_id):
        self.event_id = event_id

    # Getter method for event type
    def get_event_type(self):
        return self.event_type

    # Setter method for event type
    def set_event_type(self, event_type):
        self.event_type = event_type

    # Getter method for theme
    def get_theme(self):
        return self.theme

    # Setter method for theme
    def set_theme(self, theme):
        self.theme = theme

    # Getter method for date
    def get_date(self):
        return self.date

    # Setter method for date
    def set_date(self, date):
        self.date = date

    # Getter method for time
    def get_time(self):
        return self.time

    # Setter method for time
    def set_time(self, time):
        self.time = time

    # Getter method for duration
    def get_duration(self):
        return self.duration

    # Setter method for duration
    def set_duration(self, duration):
        self.duration = duration

    # Getter method for venue address
    def get_venue_address(self):
        return self.venue_address

    # Setter method for venue address
    def set_venue_address(self, venue_address):
        self.venue_address = venue_address

    # Getter method for client ID
    def get_client_id(self):
        return self.client_id

    # Setter method for client ID
    def set_client_id(self, client_id):
        self.client_id = client_id

    # Getter method for guest list
    def get_guest_list(self):
        return self.guest_list

    # Setter method for guest list
    def set_guest_list(self, guest_list):
        self.guest_list = guest_list

    # Getter method for suppliers
    def get_suppliers(self):
        return self.suppliers

    # Setter method for suppliers
    def set_suppliers(self, suppliers):
        self.suppliers = suppliers

    # Getter method for invoice
    def get_invoice(self):
        return self.invoice

    # Setter method for invoice
    def set_invoice(self, invoice):
        self.invoice = invoice
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
class Employee:
    """Class to represent an employee"""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        #constructor to initialize the Employee object with provided attributes
        self.name = name  #employee's name
        self.employee_id = employee_id  #employee's ID
        self.department = department  #department where the employee works
        self.job_title = job_title  #job title of the employee
        self.basic_salary = basic_salary  #basic salary of the employee
        self.age = age  #Age of the employee
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

class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id  # Unique identifier for the guest
        self.name = name  # Name of the guest
        self.address = address  # Address of the guest
        self.contact_details = contact_details  # Contact details of the guest

    # Getters and Setters

    def get_guest_id(self):
        """Get the guest's ID."""
        return self.guest_id

    def set_guest_id(self, guest_id):
        """Set the guest's ID."""
        self.guest_id = guest_id

    def get_name(self):
        """Get the guest's name."""
        return self.name

    def set_name(self, name):
        """Set the guest's name."""
        self.name = name

    def get_address(self):
        """Get the guest's address."""
        return self.address

    def set_address(self, address):
        """Set the guest's address."""
        self.address = address

    def get_contact_details(self):
        """Get the guest's contact details."""
        return self.contact_details

    def set_contact_details(self, contact_details):
        """Set the guest's contact details."""
        self.contact_details = contact_details
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

class Venue:
    """class to represent a venue"""
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id  # Unique identifier for the venue
        self.name = name  # Name of the venue
        self.address = address  # Address of the venue
        self.contact = contact  # Contact information for the venue
        self.min_guests = min_guests  # Minimum number of guests the venue can accommodate
        self.max_guests = max_guests  # Maximum number of guests the venue can accommodate

    # Getters and Setters

    def get_venue_id(self):
        """Get the venue's ID."""
        return self.venue_id

    def set_venue_id(self, venue_id):
        """Set the venue's ID."""
        self.venue_id = venue_id

    def get_name(self):
        """Get the venue's name."""
        return self.name

    def set_name(self, name):
        """Set the venue's name."""
        self.name = name

    def get_address(self):
        """Get the venue's address."""
        return self.address

    def set_address(self, address):
        """Set the venue's address."""
        self.address = address

    def get_contact(self):
        """Get the venue's contact information."""
        return self.contact

    def set_contact(self, contact):
        """Set the venue's contact information."""
        self.contact = contact

    def get_min_guests(self):
        """Get the minimum number of guests the venue can accommodate."""
        return self.min_guests

    def set_min_guests(self, min_guests):
        """Set the minimum number of guests the venue can accommodate."""
        self.min_guests = min_guests

    def get_max_guests(self):
        """Get the maximum number of guests the venue can accommodate."""
        return self.max_guests

    def set_max_guests(self, max_guests):
        """Set the maximum number of guests the venue can accommodate."""
        self.max_guests = max_guests
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

class Client:
    """Class to represent client"""
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id  # Unique identifier for the client
        self.name = name  # Name of the client
        self.address = address  # Address of the client
        self.contact_details = contact_details  # Contact details of the client
        self.budget = budget  # Budget allocated by the client

    # Getter method for client ID
    def get_client_id(self):
        return self.client_id

    # Setter method for client ID
    def set_client_id(self, client_id):
        self.client_id = client_id

    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for name
    def set_name(self, name):
        self.name = name

    # Getter method for address
    def get_address(self):
        return self.address

    # Setter method for address
    def set_address(self, address):
        self.address = address

    # Getter method for contact details
    def get_contact_details(self):
        return self.contact_details

    # Setter method for contact details
    def set_contact_details(self, contact_details):
        self.contact_details = contact_details

    # Getter method for budget
    def get_budget(self):
        return self.budget

    # Setter method for budget
    def set_budget(self, budget):
        self.budget = budget
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

class Supplier:
    """class to represent a supplier"""
    def __init__(self, supplier_id, name, address, contact_details, service_type):
        self._supplier_id = supplier_id  #unique identifier for the supplier
        self._name = name  # Name of the supplier
        self._address = address  # Address of the supplier
        self._contact_details = contact_details  # Contact details of the supplier
        self._service_type = service_type  # Type of service provided by the supplier

    # Getter and setter for supplier ID
    def supplier_id(self):
        return self._supplier_id

    def supplier_id(self, value):
        self._supplier_id = value

    # Getter and setter for name
    def name(self):
        return self._name

    def name(self, value):
        self._name = value

    # Getter and setter for address
    def address(self):
        return self._address

    def address(self, value):
        self._address = value

    # Getter and setter for contact details
    def contact_details(self):
        return self._contact_details

    def contact_details(self, value):
        self._contact_details = value

    # Getter and setter for service type
    def service_type(self):
        return self._service_type

    def service_type(self, value):
        self._service_type = value
# Function to add a supplier
def add_supplier():
    supplier = Supplier(sup_id_entry.get(), sup_name_entry.get(), sup_address_entry.get(), sup_contact_entry.get(),service_type_entry.get())
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

def clear_supplier_fields():
    # Assuming you have these entry fields as global variables or accessible in this scope.
    sup_id_entry.delete(0, tk.END)
    sup_name_entry.delete(0, tk.END)
    sup_address_entry.delete(0, tk.END)
    sup_contact_entry.delete(0, tk.END)
    service_type_entry.delete(0, tk.END)

# Function to modify supplier details
def modify_supplier():
    pass
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
class SalesPerson(Employee):
    """Handles sales operations with specific targets."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, sales_target):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.sales_target = sales_target

    def calculate_commission(self, sales):
        """Calculate commission based on sales."""
        return sales * 0.05  # Assuming a 5% commission rate

    # Getters and Setters
    def get_sales_target(self):
        return self.sales_target

    def set_sales_target(self, sales_target):
        self.sales_target = sales_target


class SalesManager(SalesPerson):
    """Manages a sales team and their targets."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, sales_target, team_size):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, sales_target)
        self.team_size = team_size

    def motivate_team(self):
        """Motivate the sales team to achieve targets."""
        print("Let's exceed our sales targets this quarter!")

    # Getter and Setter
    def get_team_size(self):
        return self.team_size

    def set_team_size(self, team_size):
        self.team_size = team_size


class MarketingManager(Employee):
    """Handles marketing budgets and campaign strategies."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, marketing_budget, campaigns_handled):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.marketing_budget = marketing_budget
        self.campaigns_handled = campaigns_handled

    def allocate_budget(self, budget):
        """Allocate or update the marketing budget."""
        self.marketing_budget = budget

    # Getters and Setters
    def get_marketing_budget(self):
        return self.marketing_budget

    def set_marketing_budget(self, marketing_budget):
        self.marketing_budget = marketing_budget

    def get_campaigns_handled(self):
        return self.campaigns_handled

    def set_campaigns_handled(self, campaigns_handled):
        self.campaigns_handled = campaigns_handled


class Marketer(Employee):
    """Involved in executing marketing campaigns."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, campaigns_involved):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.campaigns_involved = campaigns_involved

    # Getters and Setters
    def get_campaigns_involved(self):
        return self.campaigns_involved

    def set_campaigns_involved(self, campaigns_involved):
        self.campaigns_involved = campaigns_involved


class Accountant(Employee):
    """Manages company finances and budget reports."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, managed_budgets):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.managed_budgets = managed_budgets

    def report_financials(self):
        """Report the financial status of the company."""
        print("Generating financial report...")

    # Getters and Setters
    def get_managed_budgets(self):
        return self.managed_budgets

    def set_managed_budgets(self, managed_budgets):
        self.managed_budgets = managed_budgets


class Designer(Employee):
    """Designs event setups and visual presentations."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, design_projects):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.design_projects = design_projects

    # Getters and Setters
    def get_design_projects(self):
        return self.design_projects

    def set_design_projects(self, design_projects):
        self.design_projects = design_projects


class CateringCompany(Supplier):
    """A specialized Supplier subclass for catering services."""
    def __init__(self, supplier_id, name, address, contact_details, menu_offered, min_guests, max_guests):
        super().__init__(supplier_id, name, address, contact_details, 'Catering')
        self.menu_offered = menu_offered
        self.min_guests = min_guests
        self.max_guests = max_guests

    def add_dish(self, dish):
        """Add a dish to the menu if it's not already offered."""
        if dish not in self.menu_offered:
            self.menu_offered.append(dish)

    def remove_dish(self, dish):
        """Remove a dish from the menu if it exists."""
        if dish in self.menu_offered:
            self.menu_offered.remove(dish)

    def get_menu_offered(self):
        return self.menu_offered

    def set_menu_offered(self, menu_offered):
        self.menu_offered = menu_offered

    def get_min_guests(self):
        return self.min_guests

    def set_min_guests(self, min_guests):
        self.min_guests = min_guests

    def get_max_guests(self):
        return self.max_guests

    def set_max_guests(self, max_guests):
        self.max_guests = max_guests


class CleaningCompany(Supplier):
    """A specialized Supplier subclass for cleaning services."""
    def __init__(self, supplier_id, name, address, contact_details, cleaning_standards, tools_provided):
        super().__init__(supplier_id, name, address, contact_details, 'Cleaning')
        self.cleaning_standards = cleaning_standards
        self.tools_provided = tools_provided

    def get_cleaning_standards(self):
        return self.cleaning_standards

    def set_cleaning_standards(self, cleaning_standards):
        self.cleaning_standards = cleaning_standards

    def get_tools_provided(self):
        return self.tools_provided

    def set_tools_provided(self, tools_provided):
        self.tools_provided = tools_provided


class DecorationsCompany(Supplier):
    """A specialized Supplier subclass for decorations services."""
    def __init__(self, supplier_id, name, address, contact_details, decoration_styles):
        super().__init__(supplier_id, name, address, contact_details, 'Decorations')
        self.decoration_styles = decoration_styles

    def add_style(self, style):
        """Add a decoration style if it's not already offered."""
        if style not in self.decoration_styles:
            self.decoration_styles.append(style)

    def remove_style(self, style):
        """Remove a decoration style if it exists."""
        if style in self.decoration_styles:
            self.decoration_styles.remove(style)

    def get_decoration_styles(self):
        return self.decoration_styles

    def set_decoration_styles(self, decoration_styles):
        self.decoration_styles = decoration_styles


class EntertainmentCompany(Supplier):
    """A specialized Supplier subclass for entertainment services."""
    def __init__(self, supplier_id, name, address, contact_details, entertainment_types):
        super().__init__(supplier_id, name, address, contact_details, 'Entertainment')
        self.entertainment_types = entertainment_types

    def add_entertainment_type(self, type):
        """Add an entertainment type if it's not already provided."""
        if type not in self.entertainment_types:
            self.entertainment_types.append(type)

    def remove_entertainment_type(self, type):
        """Remove an entertainment type if it exists."""
        if type in self.entertainment_types:
            self.entertainment_types.remove(type)

    def get_entertainment_types(self):
        return self.entertainment_types

    def set_entertainment_types(self, entertainment_types):
        self.entertainment_types = entertainment_types


class FurnitureSupplyCompany(Supplier):
    """A specialized Supplier subclass for furniture supply services."""
    def __init__(self, supplier_id, name, address, contact_details, furniture_catalog, delivery_options):
        super().__init__(supplier_id, name, address, contact_details, 'Furniture Supply')
        self.furniture_catalog = furniture_catalog
        self.delivery_options = delivery_options

    def add_item_to_catalog(self, item):
        """Add a furniture item to the catalog if it's not already available."""
        if item not in self.furniture_catalog:
            self.furniture_catalog.append(item)

    def remove_item_from_catalog(self, item):
        """Remove a furniture item from the catalog if it exists."""
        if item in self.furniture_catalog:
            self.furniture_catalog.remove(item)

    def get_furniture_catalog(self):
        return self.furniture_catalog

    def set_furniture_catalog(self, furniture_catalog):
        self.furniture_catalog = furniture_catalog

    def get_delivery_options(self):
        return self.delivery_options

    def set_delivery_options(self, delivery_options):
        self.delivery_options = delivery_options


