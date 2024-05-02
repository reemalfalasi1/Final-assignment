import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import pickle

class Venue:
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
def main():
    root = tk.Tk()
    root.title("Management System")

    # Create notebook
    notebook = tk.ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create frames for each entity
    venue_frame = tk.Frame(notebook)
    notebook.add(venue_frame, text='Venues')
    populate_venue_frame(venue_frame)
    root.mainloop()
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
if __name__ == "__main__":
    main()


