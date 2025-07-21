# Assignment3
Task 1: Calculate Factorial Using a Function<br>

Problem Summary:<br>

Define a function factorial(n) using loop or recursion.<br>
Return the result.<br>
Call the function with a number (e.g. 5) and print the result.<br><br>
def factorial(n):
    fact = 1
    while n>0:
        fact *=n
        n -= 1
    return fact

num= int(input("Enter a number: "))

res = factorial(num)
print("factorial of",num," is : ",res)
<br><br>

Task 2: Using the Math Module for Calculations<br>

Problem Summary:<br>

Ask the user to input a number.<br>
Use the math module to:<br>
Find square root<br>
Natural logarithm (log base e)<br>
Sine (value in radians)<br>
Print results<br><br>
from math import *
num = input("Enter a number :")
num = int(num)
print(num)

# Square root of no.
print("Square root : ",sqrt(num))

# Logarithm of no.
print("Log : ",log(num))

# Sine no. in radians
print("Sine : ",sin(num))



