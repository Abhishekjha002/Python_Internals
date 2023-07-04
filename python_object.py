"""
    Everything in python is an Object and we can check this using type operator.
    PyObject represent the base structure for all Python objects.
    PyObject is defined as a struct in C language.
"""


# ll = [1,2,3,4]
# print(type(ll))

# a = 1
# print(type(a))

# str = "HELLO!!"
# print(type(str))


# Use dir methods to get all the variables and methods

# print(dir(ll))


"""
    In python, every object has an id for its identity. 
    The id of an object is always unique and constant for this object during its lifetime.
    you can check the id of object using id method.
"""


# n1 = 5
# print(id(n1))


# n2 = 10
# print(id(n2))

# n2 = n1
# print(id(n2))


"""
Mutable data types in Python: Numbers, Boolean, String, Bytes, Tuples
Immutable data types in python: List, Dictionary, Sets
"""

"""
    How variables actually work in Python?
    Variable in C is a container holding value
    Variable in python is label sticker on a container
    When you delete a variable actualt object is not deleted, only the reference is removed and 
    reference count field of an object is decremented. When all reference are deleted 
    and goes out of scope, the reference count become zero and the object is garbage collected. 
    That's the reason int are immutable
"""

"""
    Integers are immutable becoz once they are created you can't change its state.
"""

import sys
# x = 45

# print(hex(id(x)))

# print(sys.getrefcount(x))
# y = x
# print(sys.getrefcount(x))

# del x
# print(sys.getrefcount(y))


"""
    We will see container data types like lists which can hold other data types.
    Lists can hold multiple values and their internal state can be changed by adding or removing elements.
    Instead of PyObject, the basic structure for container type objects is PyVarObject.
    PyVarObject is just a pyobject with an additional size field.
    The size field is used to store the number of elements that the container object holds.
    The value field will be a pointer to the memory location of the storage array where 
    actual elements are store. Notice that the element is not directly stored in this array instead,
    only pointers to the elements are stored.
    Array indexing become easy when we store pointer as int, boolean, string etc. all have sme size of pointer
"""

# x = [1,2,3]

# print(sys.getrefcount(x))

# y = x

# print(sys.getrefcount(x))


# x.append(1)

# print(x)
# print(y)


"""
Interning: 
    Interning is the way Python optimizes the memory used by a program by 
    referencing the same space in memory of a numeric (with some exceptions) or 
    string variable with the same data as a previously created variable. 
"""

# x and y reference to the same object

# x = None
# y = None

# print(hex(id(x)), hex(id(y)))


"""
    At start, python pre-loads or caches a few the most commonly used objects,
    so that it doesn't have to re-create them when needed.
    Integers in the inclusive range -5 to 256 are also interned
"""

# x = 42
# y = 42

# print(hex(id(x)), hex(id(y)))

# x = 257
# y = 257

# print(hex(id(x)), hex(id(y)))


"""
    In case of strings, strings that looks similar are also interned
"""

# a = "some string"
# b = "some string"

# print(hex(id(a)), hex(id(b)))

"""
    Pyhton has two ways to check equality objects:
    1. ==
    2. IS

    1. == opertor compare the objects by element to element
    2. IS operator compare the address

    Basically, IS operator is used to check if a variable is None, since only one None object is ever
    created by the python interpreter during the lifetime of your program.
"""


"""
    How variables are passed to functions?
    We defined a list with element [1,2,3]. This list is passed as an argument to the function.
    Within the function, we will assign a new list to the input paramater.
    Functions have seperate scope, Objects are passed by reference to the function,
    so mylist and nums will point to the same list object, within a function when a new list is assign
    to 'mylist', a new list object is created and mylist will point to this new list.
    When functions returns, the mylist goes out of scope and newly created list will also
    be removed by memory manager because there are no reference to it. This means assigning new value
    within the function wont change our original value outside the function.
"""


# def assign_new_list(mylist):
#     mylist = [42, 34, 27]

# nums = [1,2,3]
# assign_new_list(nums)
# print(nums)


"""
    Suppose if we actually wanted to change the original list from within the function,
    WE NEED TO USED THE METHODS DEFINED ON OBJECTS.
"""

# def add_ten_to_list(mylist):
#     mylist.append(10)

# nums = [1,2,3]
# add_ten_to_list(nums)
# print(nums)


"""
    Default Mutable Parameters:
    Python allows you to define default value for a parameter, when defining the function

    Remember everything in python is an object, even functions.
    The function is an object of the 'function' class
    and function object is created at some memory address.
    Function objects has a '__default__' attribute, which stores the default value as a tuple
    Consider this is the function object created in memory. 
    It has a 'my_list' attribute.
    The function object gets created when python executes the function definition that is 'def' statement
    as part of this python evaluated the default arguments.
    In our case, an empty list object is created somewhere in the memory and
    reference to it is stored is 'my_list' attribute of the function object.
    Note that function body is not evaluated at this point 
    it only happens when you call the function.
    Like any other object, the function name 'add_two_to_list' will be a reference to this function object
    When we call the function for the first time 2 is added to default list and variable 
    first become reference to this list. Same thing happens again when you call the function
    2 is again added to the default list and variable second becomes another reference to it.
    Note that we are using list here, but this behaviour is same for any mutable container
    types like dictionary, sets etc. 
    We wont have any unexpected behaviour if we use immutable objects like integer or string as default
    parameters because there is no way to mutate their internal state.
    A better approach is to use None as the default value for mutable objects
"""

# def add_two_to_list(my_list=[]):
#     my_list.append(2)
#     return my_list

# a = add_two_to_list()
# print(a)

# b = add_two_to_list()
# print(b)

# def add_two_to_list(my_list=None):
#     my_list = my_list or []
#     my_list.append(2)
#     return my_list


# a = add_two_to_list()
# print(a)

# b = add_two_to_list()
# print(b)



"""
    The += operator
"""

# x = [1,2,3]

# y = x

# expression is evaluated from right to left. A new memory block is created for below.
# x = x + [4, 5]

# x = [1,2,3]
# y = x
# # += operator use the list method __iadd__ which take self as x and new list as [4,5]
# # return the value at last which is x.
# x += [4,5]

# print(x)
# print(y)




"""
    Mutable objects in python
"""


# x = 1, [1,2]
# x[1].append(3)
# print(x)


x = 1, [1, 2]

# It uses __iadd__ method which will return x and try to change the value of tuple x
# with the same address but tuple can't be changed 
x[1] += [3]
print(x)










