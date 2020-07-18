'''Q 1. Write a Python function to find the Max of three numbers.'''

def max(num1,num2,num3):
    if num1<num2 and num1>num3:
        return num2
    elif num1>num2 and num1>num3:
        return num1
    else:
        return num3
        
        
print ("maximum number is",(max(75,98,37))) #Caliing the function.

