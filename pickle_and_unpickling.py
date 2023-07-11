"""
    Pickle is a module in Python that is primarily used to serialize and de-serialize 
    a Python object structure. Both pickling and unpickling become essential when we 
    have to transfer Python objects from one system to another.

    Pickling is a process by which the object structure in Python is serialized. 
    A Python object is converted into a byte stream when it undergoes pickling.

    Unpickling is a process by which original Python objects are retrieved from the 
    stored string representation i.e., from the pickle file. It converts the byte 
    stream into a Python object.

"""

import pickle

cars = ["BMW", "AUDI", "Maruti Suzuki"]

file_name = "car.pkl"
# file_obj = open(file_name, "wb")
# pickle.dump(cars, file_obj)
# file_obj.close()

file_obj = open(file_name, 'rb')
my_car = pickle.load(file_obj)
print(my_car)
