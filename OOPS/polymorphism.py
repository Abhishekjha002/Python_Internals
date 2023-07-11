"""
    Polymorphism: Many forms.
    We achived polymorphism in python by four ways:
    1. Duck Typing
    2. Operator overloading
    3. Method overloading
    4. Method overriding
"""


# Duck Typing

class PyCharm:

    def execute(self):
        print("Compiling!!!")
        print("Executing!!!")


class VSCode:

    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compiling!!!")
        print("Executing!!!")

class Laptop:

    def code(self, ide):
        ide.execute()

# ide = PyCharm()
ide = VSCode()
obj = Laptop()
# obj.code(ide)



# 2. Operator Overloading

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1,m2)

    def __str__(self):
        return "{} {}".format(self.m1, self.m2)
    
    def __gt__(self, other):
        if self.m1 + self.m2 > other.m1 + other.m2:
            return True
        return False

a = 10
b = 20
# print(a + b)
# # Internally 
# print(int.__add__(a, b))

# s1 = Student(50, 70)
# s2 = Student(70, 80)

# s3 = s1 + s2

# print(a)
# # Internally
# print(a.__str__())

# print(s3)

# if s1 > s2:
#     print("s1 is greater!!!")
# else:
#     print("s2 is greater!!!")

# Method overloading

def add(a=None, b=None):
    # Checks if both parameters are available
    # if statement will be executed if only one parameter is available
    if a != None and b == None:
        print(a)
    # else will be executed if both are available and returns addition of two
    else:
        print(a+b)
 
 
# two arguments are passed, returns addition of two
add(2, 3)
# only one argument is passed, returns a
add(2)



from multipledispatch import dispatch
 
# passing one parameter
 
 
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)
 
# passing two parameters
 
 
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)
 
# you can also pass data type of any value as per requirement
 
 
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)
 
 
# calling product method with 2 arguments
product(2, 3)  # this will give output of 6
 
# calling product method with 3 arguments but all int
product(2, 3, 2)  # this will give output of 12
 
# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3) 




# 4. Method overiding is achieved by inheritance 








