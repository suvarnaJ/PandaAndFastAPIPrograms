# Parent class
class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("Updated balance:", self.balance)

    def display_balance(self):
        print("Account Balance:", self.balance)

    def account_details(self):
        print("Account Number :", self.account_number)
        print("Holder Name    :", self.holder_name)
        print("Balance        :", self.balance)


# Child class 1
class SavingsAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def display_savings_details(self):
        self.account_details()
        print("Interest Rate  :", self.interest_rate, "%")


# Child class 2
class CurrentAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def display_current_details(self):
        self.account_details()
        print("Overdraft Limit:", self.overdraft_limit)


# Child class 3
class SalaryAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance,
                 employer, monthly_salary):
        super().__init__(account_number, holder_name, balance)
        self.employer = employer
        self.monthly_salary = monthly_salary

    def display_salary_details(self):
        self.account_details()
        print("Employer       :", self.employer)
        print("Monthly Salary :", self.monthly_salary)


# --------------------------------------------------
# Create Savings Account objects
# --------------------------------------------------

savings1 = SavingsAccount(
    "SA1001",
    "Suvarna",
    50000,
    6.5
)

savings2 = SavingsAccount(
    "SA1002",
    "Priya",
    75000,
    7.0
)


# --------------------------------------------------
# Create Current Account objects
# --------------------------------------------------

current1 = CurrentAccount(
    "CA2001",
    "Raj",
    100000,
    50000
)

current2 = CurrentAccount(
    "CA2002",
    "Amit",
    150000,
    75000
)


# --------------------------------------------------
# Create Salary Account objects
# --------------------------------------------------

salary1 = SalaryAccount(
    "SAL3001",
    "Neha",
    60000,
    "TCS",
    85000
)

salary2 = SalaryAccount(
    "SAL3002",
    "Rahul",
    80000,
    "Infosys",
    95000
)


# --------------------------------------------------
# Demonstrate Savings Account
# --------------------------------------------------

print("\n===== SAVINGS ACCOUNT =====")

savings1.display_savings_details()

print("\nDepositing money...")
savings1.deposit(10000)

print("\nDisplaying balance...")
savings1.display_balance()


# --------------------------------------------------
# Demonstrate Current Account
# --------------------------------------------------

print("\n===== CURRENT ACCOUNT =====")

current1.display_current_details()

print("\nDepositing money...")
current1.deposit(20000)

print("\nDisplaying balance...")
current1.display_balance()


# --------------------------------------------------
# Demonstrate Salary Account
# --------------------------------------------------

print("\n===== SALARY ACCOUNT =====")

salary1.display_salary_details()

print("\nDepositing money...")
salary1.deposit(15000)

print("\nDisplaying balance...")
salary1.display_balance()


# --------------------------------------------------
# Demonstrate inherited behavior on other objects
# --------------------------------------------------

print("\n===== OTHER ACCOUNTS =====")

savings2.display_savings_details()

print()

current2.display_current_details()

print()

salary2.display_salary_details()