import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import pickle
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

def main():
    root = tk.Tk()
    root.title("Management System")

    # Create notebook
    notebook = tk.ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create frames for each entity
    supplier_frame = tk.Frame(notebook)
    notebook.add(supplier_frame, text='Suppliers')
    populate_supplier_frame(supplier_frame)
    root.mainloop()
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

if __name__ == "__main__":
    main()