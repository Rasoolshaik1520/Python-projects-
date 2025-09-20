import math

def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def modulo(x, y):
    return x % y
def square_root(x):
    return math.sqrt(x)
def power(x, y):
    return x**y
