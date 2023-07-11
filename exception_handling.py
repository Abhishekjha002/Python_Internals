class MyError(Exception):
    pass

a = 10
b = 10

try:
    z = a / b
    if z == 1:
        raise MyError("Number are equal!!!")
except Exception as e:
    print(e)
else:
    print("Done with the divison part")
finally:
    print("Now please releadse memory")


