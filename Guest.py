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
