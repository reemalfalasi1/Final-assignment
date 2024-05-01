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
