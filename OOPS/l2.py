class Employee:

    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = self.first_name.lower() + "." + self.last_name.lower() + "@company.com"

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(float(self.pay) * self.raise_amt)


class Developer(Employee):
    
    raise_amt = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        # super().__init__(first_name, last_name, pay) 
        Employee.__init__(self, first_name, last_name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        self.employees = employees or []

    def add_emps(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print("--> ", emp.full_name())


dev_1 = Developer("Abhishek", "Jha", 50000, "Python")
dev_2 = Developer("Ria", "Jha", 60000, "Java")

# print(dev_1.email)
# print(dev_1.full_name())
# print(isinstance(dev_1, Employee))

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


mgr_1 = Manager("Kumudini", "Jha", 70000, [dev_1, dev_2])

mgr_1.print_employees()
mgr_1.remove_emp(dev_1)
print("New Configuration")
mgr_1.print_employees()

# print(issubclass(Developer, Employee))
