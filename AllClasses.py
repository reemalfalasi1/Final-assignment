class Employee:
    """Class to represent an employee"""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        #constructor to initialize the Employee object with provided attributes
        self.name = name  #employee's name
        self.employee_id = employee_id  #employee's ID
        self.department = department  #department where the employee works
        self.job_title = job_title  #job title of the employee
        self.basic_salary = basic_salary  #basic salary of the employee
        self.age = age  # Age of the employee
        self.date_of_birth = date_of_birth #date of birth of the employee
        self.passport_details = passport_details#passport details of the employee

    # Getters and Setters for each attribute
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_job_title(self):
        return self.job_title

    def set_job_title(self, job_title):
        self.job_title = job_title

    def get_basic_salary(self):
        return self.basic_salary

    def set_basic_salary(self, basic_salary):
        self.basic_salary = basic_salary

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def get_passport_details(self):
        return self.passport_details

    def set_passport_details(self, passport_details):
        self.passport_details = passport_details


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


class SalesPerson(Employee):
    """Handles sales operations with specific targets."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, sales_target):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.sales_target = sales_target

    def calculate_commission(self, sales):
        """Calculate commission based on sales."""
        return sales * 0.05  # Assuming a 5% commission rate

    # Getters and Setters
    def get_sales_target(self):
        return self.sales_target

    def set_sales_target(self, sales_target):
        self.sales_target = sales_target


class SalesManager(SalesPerson):
    """Manages a sales team and their targets."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, sales_target, team_size):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, sales_target)
        self.team_size = team_size

    def motivate_team(self):
        """Motivate the sales team to achieve targets."""
        print("Let's exceed our sales targets this quarter!")

    # Getter and Setter
    def get_team_size(self):
        return self.team_size

    def set_team_size(self, team_size):
        self.team_size = team_size


class MarketingManager(Employee):
    """Handles marketing budgets and campaign strategies."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, marketing_budget, campaigns_handled):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.marketing_budget = marketing_budget
        self.campaigns_handled = campaigns_handled

    def allocate_budget(self, budget):
        """Allocate or update the marketing budget."""
        self.marketing_budget = budget

    # Getters and Setters
    def get_marketing_budget(self):
        return self.marketing_budget

    def set_marketing_budget(self, marketing_budget):
        self.marketing_budget = marketing_budget

    def get_campaigns_handled(self):
        return self.campaigns_handled

    def set_campaigns_handled(self, campaigns_handled):
        self.campaigns_handled = campaigns_handled


class Marketer(Employee):
    """Involved in executing marketing campaigns."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, campaigns_involved):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.campaigns_involved = campaigns_involved

    # Getters and Setters
    def get_campaigns_involved(self):
        return self.campaigns_involved

    def set_campaigns_involved(self, campaigns_involved):
        self.campaigns_involved = campaigns_involved


class Accountant(Employee):
    """Manages company finances and budget reports."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, managed_budgets):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.managed_budgets = managed_budgets

    def report_financials(self):
        """Report the financial status of the company."""
        print("Generating financial report...")

    # Getters and Setters
    def get_managed_budgets(self):
        return self.managed_budgets

    def set_managed_budgets(self, managed_budgets):
        self.managed_budgets = managed_budgets


class Designer(Employee):
    """Designs event setups and visual presentations."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, design_projects):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.design_projects = design_projects

    # Getters and Setters
    def get_design_projects(self):
        return self.design_projects

    def set_design_projects(self, design_projects):
        self.design_projects = design_projects


class Handyman(Employee):
    """Performs maintenance and repair tasks for event setups."""
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)

    def perform_maintenance(self):
        """Perform routine maintenance tasks."""
        print("Performing maintenance tasks...")


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
        super().__init__(supplier_id, name, address, contact_details, 'Furniture Supply')
        self.furniture_catalog = furniture_catalog
        self.delivery_options = delivery_options

    def add_item_to_catalog(self, item):
        """Add a furniture item to the catalog if it's not already available."""
        if item not in self.furniture_catalog:
            self.furniture_catalog.append(item)

    def remove_item_from_catalog(self, item):
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


class Photographer(Supplier):
    """A specialized Supplier subclass for photography services."""
    def __init__(self, supplier_id, name, address, contact_details, photography_styles, services_offered):
        super().__init__(supplier_id, name, address, contact_details, 'Photography')
        self.photography_styles = photography_styles
        self.services_offered = services_offered

    def add_photography_style(self, style):
        """Add a photography style if it's not already offered."""
        if style not in self.photography_styles:
            self.photography_styles.append(style)

    def remove_photography_style(self, style):
        """Remove a photography style if it exists."""
        if style in self.photography_styles:
            self.photography_styles.remove(style)

    def get_photography_styles(self):
        return self.photography_styles

    def set_photography_styles(self, photography_styles):
        self.photography_styles = photography_styles

    def get_services_offered(self):
        return self.services_offered

    def set_services_offered(self, services_offered):
        self.services_offered = services_offered


class TransportationCompany(Supplier):
    """A specialized Supplier subclass for transportation services."""
    def __init__(self, supplier_id, name, address, contact_details, vehicle_types, max_capacity):
        super().__init__(supplier_id, name, address, contact_details, 'Transportation')
        self.vehicle_types = vehicle_types
        self.max_capacity = max_capacity

    def add_vehicle_type(self, type):
        """Add a vehicle type if it's not already offered."""
        if type not in self.vehicle_types:
            self.vehicle_types.append(type)

    def remove_vehicle_type(self, type):
        """Remove a vehicle type if it exists."""
        if type in self.vehicle_types:
            self.vehicle_types.remove(type)

    def get_vehicle_types(self):
        return self.vehicle_types

    def set_vehicle_types(self, vehicle_types):
        self.vehicle_types = vehicle_types

    def get_max_capacity(self):
        return self.max_capacity

    def set_max_capacity(self, max_capacity):
        self.max_capacity = max_capacity
