import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import pickle

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
def main():
    root = tk.Tk()
    root.title("Management System")

    # Create notebook
    notebook = tk.ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create frames for each entity
    event_frame = tk.Frame(notebook)
    notebook.add(event_frame, text='Events')
    populate_event_frame(event_frame)
    root.mainloop()
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