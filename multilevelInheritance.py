# Parent Class
class Person:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)


# Child Class of Person
class Employee(Person):

    def __init__(self, name, age, city, employee_id, salary, company):
        super().__init__(name, age, city)

        self.employee_id = employee_id
        self.salary = salary
        self.company = company

    def display_employee_details(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Company:", self.company)


# Child Class of Employee
class Developer(Employee):

    def __init__(
        self,
        name,
        age,
        city,
        employee_id,
        salary,
        company,
        language,
        framework,
        experience
    ):
        super().__init__(
            name,
            age,
            city,
            employee_id,
            salary,
            company
        )

        self.language = language
        self.framework = framework
        self.experience = experience

    def display_developer_details(self):
        print("Programming Language:", self.language)
        print("Framework:", self.framework)
        print("Experience:", self.experience, "years")

    def write_code(self):
        print(self.name, "is writing", self.language, "code.")

    def display_all_details(self):
        self.display_person_details()
        self.display_employee_details()
        self.display_developer_details()


# --------------------------------------------------
# Creating 5 Developer Objects
# --------------------------------------------------

developer1 = Developer(
    "Amit", 30, "Pune",
    "EMP101", 1200000, "ABC Technologies",
    "Java", "Spring Boot", 7
)

developer2 = Developer(
    "Priya", 28, "Mumbai",
    "EMP102", 1100000, "XYZ Solutions",
    "Python", "Django", 5
)

developer3 = Developer(
    "Rahul", 32, "Bangalore",
    "EMP103", 1500000, "TechCorp",
    "Java", "Spring Boot", 9
)

developer4 = Developer(
    "Sneha", 27, "Delhi",
    "EMP104", 1000000, "Infosys",
    "Python", "Flask", 4
)

developer5 = Developer(
    "Karan", 35, "Hyderabad",
    "EMP105", 1800000, "TCS",
    "JavaScript", "React", 10
)


# --------------------------------------------------
# Demonstrating Developer object accessing all levels
# --------------------------------------------------

print("========== DEVELOPER 1 ==========")

# Person level properties
print("Name:", developer1.name)
print("Age:", developer1.age)
print("City:", developer1.city)

# Employee level properties
print("Employee ID:", developer1.employee_id)
print("Salary:", developer1.salary)
print("Company:", developer1.company)

# Developer level properties
print("Language:", developer1.language)
print("Framework:", developer1.framework)
print("Experience:", developer1.experience)

print("\n--- Calling methods from all levels ---")

# Method inherited from Person
developer1.display_person_details()

# Method inherited from Employee
developer1.display_employee_details()

# Method defined in Developer
developer1.display_developer_details()

# Another Developer method
developer1.write_code()


# --------------------------------------------------
# Display all 5 developers
# --------------------------------------------------

print("\n\n========== ALL DEVELOPERS ==========")

developers = [
    developer1,
    developer2,
    developer3,
    developer4,
    developer5
]

for developer in developers:
    print("\n----------------------------")
    developer.display_all_details()