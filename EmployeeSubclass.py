import EmployeeSubclass
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
