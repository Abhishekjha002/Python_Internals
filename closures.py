"""
    nonlocal: It is the varible which is not in global level as well as local level
"""


# a = 30

# def func1():
#     x = 30
#     def func2():
#         nonlocal x 
#         x = 25
#     func2()
#     print(x)

# func1()


"""
    Closure: 
    Closure in Python is an inner function object, a function that behaves like an object, 
    that remembers and has access to variables in the local scope in which it was created even 
    after the outer function has finished executing. It can also be defined as a means of binding data 
    to a function (linking / attaching the data with the function so that they are together), 
    without passing it as a parameter.
"""


def outer():
    x = 45
    message = "Hello"

    def inner(msg):
        print(message, msg)

    return inner

closure_method = outer()
# print(closure_method)
closure_method("Ram")