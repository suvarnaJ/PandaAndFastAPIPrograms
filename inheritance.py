# Parent Class
class Employee:

    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    # Parent class method
    def display_details(self):
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Salary      :", self.salary)
        print("Department  :", self.department)

    # Parent class method
    def calculate_salary(self):
        print("Annual Salary:", self.salary)


# Child Class - Developer
class Developer(Employee):

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        programming_language
    ):
        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        self.programming_language = programming_language

    def write_code(self):
        print(
            self.name,
            "is developing software using",
            self.programming_language
        )


# Child Class - Manager
class Manager(Employee):

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        team_size
    ):
        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        self.team_size = team_size

    def manage_team(self):
        print(
            self.name,
            "is managing a team of",
            self.team_size,
            "employees"
        )


# Child Class - HR
class HR(Employee):

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        region
    ):
        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        self.region = region

    def manage_employees(self):
        print(
            self.name,
            "is managing HR activities for",
            self.region
        )


# ==================================================
# Creating Developer Objects
# ==================================================

developer1 = Developer(
    "D101",
    "Amit",
    1200000,
    "IT",
    "Java"
)

developer2 = Developer(
    "D102",
    "Priya",
    1100000,
    "IT",
    "Python"
)


# ==================================================
# Creating Manager Objects
# ==================================================

manager1 = Manager(
    "M101",
    "Rahul",
    1800000,
    "Management",
    10
)

manager2 = Manager(
    "M102",
    "Sneha",
    2000000,
    "Management",
    15
)


# ==================================================
# Creating HR Objects
# ==================================================

hr1 = HR(
    "H101",
    "Neha",
    1000000,
    "Human Resources",
    "West India"
)

hr2 = HR(
    "H102",
    "Karan",
    950000,
    "Human Resources",
    "South India"
)


# ==================================================
# Demonstrating Developer
# ==================================================

print("\n========== DEVELOPER 1 ==========")

developer1.display_details()       # Inherited method
developer1.calculate_salary()      # Inherited method

print("Programming Language:",
      developer1.programming_language)  # Child attribute

developer1.write_code()            # Child method


print("\n========== DEVELOPER 2 ==========")

developer2.display_details()
developer2.calculate_salary()

print("Programming Language:",
      developer2.programming_language)

developer2.write_code()


# ==================================================
# Demonstrating Manager
# ==================================================

print("\n========== MANAGER 1 ==========")

manager1.display_details()         # Inherited method
manager1.calculate_salary()        # Inherited method

print("Team Size:", manager1.team_size)  # Child attribute

manager1.manage_team()             # Child method


print("\n========== MANAGER 2 ==========")

manager2.display_details()
manager2.calculate_salary()

print("Team Size:", manager2.team_size)

manager2.manage_team()


# ==================================================
# Demonstrating HR
# ==================================================

print("\n========== HR 1 ==========")

hr1.display_details()              # Inherited method
hr1.calculate_salary()             # Inherited method

print("Region:", hr1.region)       # Child attribute

hr1.manage_employees()             # Child method


print("\n========== HR 2 ==========")

hr2.display_details()
hr2.calculate_salary()

print("Region:", hr2.region)

hr2.manage_employees()