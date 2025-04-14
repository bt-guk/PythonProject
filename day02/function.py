import numbers


def return_value():
    return 1000

print(return_value())


def return_integer() -> int:
    return "Python" # should return int

def cube(num) -> int: #return type
    return num * num * num
print(cube(5))


def cube1(num: int) -> int: # argument must be integer and return must be integer
    return num * num * num
print(cube1(5))

#to return any type of numbers double, float, int..
def addition(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2

print(addition(2,2))

#there is no methodoverloading in python but it can be achieved
# by using default values for optinal parameters
def addition1(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2
print(addition1(2,2))

def addition1(num1: numbers, num2: numbers, num3: numbers = 0) -> numbers:
    return num1 + num2 + num3
print(addition1(2,2,2))