# Property Decorators - Getters, Setters, and Deleters


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    
    @full_name.setter
    def full_name(self, value):
        first, last = value.split(" ")
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print("Delete the full name")
        self.first = None
        self.last = None



emp_1 = Employee("abhishek", "jha")

# print(emp_1.email)
# emp_1.first = "ria"
# print(emp_1.email)


print(emp_1.full_name)

emp_1.full_name = "ria jha"

print(emp_1.full_name)


del emp_1.full_name

print(emp_1.full_name)