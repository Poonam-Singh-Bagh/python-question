'''Q 9. Write a Python function that takes a number as a parameter and check 
the number is prime or not.''' 

def prime_num(num):
    for i in range(2,num):
        if num % i == 0:
            return num,"is not a prime number"
    else:
        return num,"is a prime number"
        

print (prime_num(7))
   