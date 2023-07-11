"""
    List is iterable but it is not iterator.
    Iterable on high level, it is something that's loop over. 
    for example list is iterable because we loop over it.
"""

nums = [1, 2, 3]

# for num in nums:
#     print(num)

"""
    If something is iterable then it have a special method called __iter__().
    what the for loop do in the backend calling iter on our object and 
    return the iterator that we can loop over. That's why we called the list is iterable.
"""

# print(dir(nums))   # dir return many methods and variables


"""
    So we can say that list is iterable but not iterator.
    If we run __iter__ method on our list it will return an iterator. 
    So what make something a iterator, so an iterator is an object with a state so that it remembers
    where it is during its iteration and iterator also know how to get their next value with a __next__
    method. You can see in list method we dont have __next__ method. So our list doesnt 
    have a state and it doesnt know how to get its next value. So, therefore list is not a iterator.
    But when we run __iter__ method then it return an iterator for us. 
"""

# i_nums = nums.__iter__()
# i_nums = iter(nums)

# print(i_nums)
# print(dir(i_nums))

"""
    we can see iterator have two method:
    1. __iter__
    2. __next__
    If iterator have __iter__ method then we can say that iterator is iterable.
    But the difference is __iter__ return the same object.
"""

"""
    How for loop works?
"""

# iter_obj = iter(nums)
# print(iter_obj)

# while True:
#     try:
#         value = next(iter_obj)
#         print(value)
#     except StopIteration:
#         break


"""
    Construct your own iterator
"""
# class Even:

#     def __init__(self, max):
#         self.n = 2
#         self.max = max

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.n > self.max:
#             raise StopIteration
#         current = self.n
#         self.n += 2
#         return current


# obj = Even(10)
# for o in obj:
#     print(o)


"""
    Generator: In Python, a generator is a function that returns an iterator that produces a sequence 
    of values when iterated over. Generators are useful when we want to produce a large sequence of 
    values, but we don't want to store all of them in memory at once.

    The yield keyword is used to produce a value from the generator and pause the generator function's 
    execution until the next value is requested.

"""


def even_generator(max):
    n = 2
    while(n <= max):
        yield n
        n += 2

numbers = even_generator(10)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# Generator Expression

# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)

"""
    Generators are excellent mediums to represent an infinite stream of data. 
    Infinite streams cannot be stored in memory, and since generators produce only one item 
    at a time, they can represent an infinite stream of data.

    Example: Fibonacci series -> 0, 1, 1, 2, 3, 5, 8, 13, .....
"""
