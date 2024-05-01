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
