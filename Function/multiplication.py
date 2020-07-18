'''Q 3. Write a Python function to multiply all the numbers in a list.'''
def multiplication(list):
    multiple = 1
    for i in list:
        multiple *= i
    return multiple
    
multiple = multiplication([ 1,3,4,512,230])
print ("multiplication of the elements of the list is", multiple) #Caliing the function.
        
