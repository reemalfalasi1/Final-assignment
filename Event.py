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
