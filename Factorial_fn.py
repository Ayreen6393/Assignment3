def factorial(n):
    fact = 1
    while n>0:
        fact *=n
        n -= 1
    return fact

num= int(input("Enter a number: "))

res = factorial(num)
print("factorial of",num," is : ",res)

