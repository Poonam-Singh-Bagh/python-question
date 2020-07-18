'''Q 5. Write a Python function to calculate the factorial of a number.'''
def factorial(number):
    fact = 1
    for number in range(number,1,-1):
        fact *= number
    return fact
    
print (factorial(5))