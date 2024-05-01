import Supplier
class CateringCompany(Supplier):
    """A specialized Supplier subclass for catering services."""
    def __init__(self, supplier_id, name, address, contact_details, menu_offered, min_guests, max_guests):
        super().__init__(supplier_id, name, address, contact_details, 'Catering')
        self.menu_offered = menu_offered
        self.min_guests = min_guests
        self.max_guests = max_guests

    def add_dish(self, dish):
        """Add a dish to the menu if it's not already offered."""
        if dish not in self.menu_offered:
            self.menu_offered.append(dish)

    def remove_dish(self, dish):
        """Remove a dish from the menu if it exists."""
        if dish in self.menu_offered:
            self.menu_offered.remove(dish)

    def get_menu_offered(self):
        return self.menu_offered

    def set_menu_offered(self, menu_offered):
        self.menu_offered = menu_offered

    def get_min_guests(self):
        return self.min_guests

    def set_min_guests(self, min_guests):
        self.min_guests = min_guests

    def get_max_guests(self):
        return self.max_guests

    def set_max_guests(self, max_guests):
        self.max_guests = max_guests


class CleaningCompany(Supplier):
    """A specialized Supplier subclass for cleaning services."""
    def __init__(self, supplier_id, name, address, contact_details, cleaning_standards, tools_provided):
        super().__init__(supplier_id, name, address, contact_details, 'Cleaning')
        self.cleaning_standards = cleaning_standards
        self.tools_provided = tools_provided

    def get_cleaning_standards(self):
        return self.cleaning_standards

    def set_cleaning_standards(self, cleaning_standards):
        self.cleaning_standards = cleaning_standards

    def get_tools_provided(self):
        return self.tools_provided

    def set_tools_provided(self, tools_provided):
        self.tools_provided = tools_provided


class DecorationsCompany(Supplier):
    """A specialized Supplier subclass for decorations services."""
    def __init__(self, supplier_id, name, address, contact_details, decoration_styles):
        super().__init__(supplier_id, name, address, contact_details, 'Decorations')
        self.decoration_styles = decoration_styles

    def add_style(self, style):
        """Add a decoration style if it's not already offered."""
        if style not in self.decoration_styles:
            self.decoration_styles.append(style)

    def remove_style(self, style):
        """Remove a decoration style if it exists."""
        if style in self.decoration_styles:
            self.decoration_styles.remove(style)

    def get_decoration_styles(self):
        return self.decoration_styles

    def set_decoration_styles(self, decoration_styles):
        self.decoration_styles = decoration_styles


class EntertainmentCompany(Supplier):
    """A specialized Supplier subclass for entertainment services."""
    def __init__(self, supplier_id, name, address, contact_details, entertainment_types):
        super().__init__(supplier_id, name, address, contact_details, 'Entertainment')
        self.entertainment_types = entertainment_types

    def add_entertainment_type(self, type):
        """Add an entertainment type if it's not already provided."""
        if type not in self.entertainment_types:
            self.entertainment_types.append(type)

    def remove_entertainment_type(self, type):
        """Remove an entertainment type if it exists."""
        if type in self.entertainment_types:
            self.entertainment_types.remove(type)

    def get_entertainment_types(self):
        return self.entertainment_types

    def set_entertainment_types(self, entertainment_types):
        self.entertainment_types = entertainment_types


class FurnitureSupplyCompany(Supplier):
    """A specialized Supplier subclass for furniture supply services."""
    def __init__(self, supplier_id, name, address, contact_details, furniture_catalog, delivery_options):
        super().__init__(supplier_id, name, address, contact_details, 'Furniture')
        self.furniture_catalog = furniture_catalog
        self.delivery_options = delivery_options

    def add_furniture_item(self, item):
        """Add a furniture item to the catalog if it's not already included."""
        if item not in self.furniture_catalog:
            self.furniture_catalog.append(item)

    def remove_furniture_item(self, item):
        """Remove a furniture item from the catalog if it exists."""
        if item in self.furniture_catalog:
            self.furniture_catalog.remove(item)

    def get_furniture_catalog(self):
        return self.furniture_catalog

    def set_furniture_catalog(self, furniture_catalog):
        self.furniture_catalog = furniture_catalog

    def get_delivery_options(self):
        return self.delivery_options

    def set_delivery_options(self, delivery_options):
        self.delivery_options = delivery_options
