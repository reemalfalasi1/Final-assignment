class Supplier:
    """class to represent a supplier"""
    def __init__(self, supplier_id, name, address, contact_details, service_type):
        self._supplier_id = supplier_id  #unique identifier for the supplier
        self._name = name  # Name of the supplier
        self._address = address  # Address of the supplier
        self._contact_details = contact_details  # Contact details of the supplier
        self._service_type = service_type  # Type of service provided by the supplier

    # Getter and setter for supplier ID
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value

    # Getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Getter and setter for address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    # Getter and setter for contact details
    @property
    def contact_details(self):
        return self._contact_details

    @contact_details.setter
    def contact_details(self, value):
        self._contact_details = value

    # Getter and setter for service type
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
