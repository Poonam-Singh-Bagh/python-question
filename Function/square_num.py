'''Q.16. Write a Python function to create and print a list where the values 
are square of numbers between 1 and 30 (both included).'''

def square_number():
    list=[]
    i=1
    while i <= 30:
        if (i**2) <= 30:
            list.append(i**2)
        i=i+1
    return (list)

print (square_number())
    
