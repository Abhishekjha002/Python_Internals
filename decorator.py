"""
    Decorator: Python decorator is an function that takes another function 
    and add some functionality to it and then return it.

    Everything in python is an object.
"""


def display_info(func):
    def inner():
        print("Executing ", func.__name__, "function")
        func()
        print("Finished execution")
    return inner

"""
    @symbol works like below code
"""

# new_method = display_info(print_good_morning)
# print(new_method)
# new_method()

@display_info
def print_good_morning():
    print("Good Morning!!!")

def print_good_afternoon():
    print("Good Afternoon!!!")

def print_good_evening():
    print("Good Evening!!!")

def print_good_night():
    print("Good Night!!!")

# display_info(print_good_afternoon())()
# display_info(print_good_evening())()
# display_info(print_good_night())()

# print_good_morning()












"""
    Decorating function with parameters
"""


def smart_divide(func):
    def inner(a, b):
        print("Divide", a, "by", b)
        if b == 0:
            print("Divisible by zero is not possible")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a, b):
    return a / b


# x = divide(40, 2)
# print(x)

# y = divide(2, 0)
# print(y)



"""
    Chaining in decorator
"""


def star(fun):
    def inner(args):
        print("*" * 30)
        fun(args)
        print("*" * 30)
    return inner

def percent(fun):
    def inner(args):
        print("%" * 30)
        fun(args)
        print("%" * 30)
    return inner

@star
@percent
def print_message(msg):
    print(msg)

print_message("Decorators is wonderful!!!")

