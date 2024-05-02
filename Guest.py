import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import pickle

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

def main():
    root = tk.Tk()
    root.title("Management System")

    # Create notebook
    notebook = tk.ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create frames for each entity
    guest_frame = tk.Frame(notebook)
    notebook.add(guest_frame, text='Guests')
    populate_guest_frame(guest_frame)
    root.mainloop()
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
if __name__ == "__main__":
    main()