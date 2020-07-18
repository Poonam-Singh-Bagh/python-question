'''Q 2. Write a Python function to sum all the numbers in a list. '''
def total_num(list):
    sum=0
    for i in list:
        sum = sum + i
    return sum
    
    
print (total_num([ 1,3,4,512,230])) #Caliing the function.

