import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import pickle
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
def main():
    root = tk.Tk()
    root.title("Management System")

    # Create notebook
    notebook = tk.ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create frames for each entity
    client_frame = tk.Frame(notebook)
    notebook.add(client_frame, text='Clients')
    populate_client_frame(client_frame)
    root.mainloop()

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
if __name__ == "__main__":
    main()