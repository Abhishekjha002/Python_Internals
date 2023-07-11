class Employee:

    raise_amt = 1.04

    def __init__(self, first_name, last_name, email, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pay = pay

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(float(self.pay) * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    def __repr__(self):
        return "Employee ({}, {}, {})".format(self.first_name, self.last_name, self.email)
    
    def __str__(self):
        return self.full_name()



emp1 = Employee("Abhishek", "Jha", "abhishek.jha@company.com", "500000")
emp2 = Employee("Ria", "Jha", "ria.jha@company.com", "600000")

print(emp1)


# print(Employee.full_name(emp1))
# print(emp1.__dict__)
# print(Employee.__dict__)

# emp1.apply_raise()
# print(emp1.raise_amt)
# emp1.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)

