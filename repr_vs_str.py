# The goal of __repr__ is to be unambiguos
# The goal of __str__ is to be readable


import datetime

a = datetime.datetime.now()

b = str(a)

print(str(a))
print(str(b))

print(repr(a))
print(repr(b))

