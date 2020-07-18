'''Q 11. Write a Python function to check whether a number is perfect or not.'''

def perfect_num(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    if num == sum:
        return num, "is a perfect number"
    else:
        return num, "is not a perfect number"
        
        
print (perfect_num(496))

