"""
Fix the Errors #2 — Input & Math
"""
# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))5
# print(f"Sum: {x + y}")
# age = input("How old are you?")
# print(f"In 10 years you will be {int(age) + 10}")
# n = float(input("Enter a numerator: "))
# d = float(input("Enter a denominator: "))
# result = n / d
# print(f"Result: {result}")
# a = 5; b = 2
# print(f"Power: {a ^ 2}")
# print(f"Remainder: {a // b}")
# pi = 3.1415926535
# print(f"Pi is approximately {pi}")

x= 1 
y= 2
z= 3
result = (x+y) * z - (y/x)
print(f"Result: {result}")
#pemdas order of operations
#division
print(f"Division: {y/x}")
#addition
print(f"Addition: {x+y}")
#multiplication
print(f"Multiplication {(x+y)*z}")
#subtraction
print(f"Subtraction: {(x+y) *z - (y/x)}")
#modulo
print(f"Modulo: {y%x}") # the remainder of y divided by x
#power
print(f"Power:{x**y}")
# absolute value 
print(f"Absolute Value: {abs(x-y)}")
#max
print(f"Max: {max(x, y, z)}")
#min 
print(f"Min: {max(x, y, z)}")
#round
pi= 3.1415926535
print(f"Round: {round(pi)}")
#importing math library functions
from math import *
print(f"Square root of 16: {sqrt(16)}")
print(f"Ceiling of Pi: {ceil(pi)}")
print(f"Floor of pi: {floor(pi)}")