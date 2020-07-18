6'''Q 6. Write a Python function to check whether a number is in a given range.'''
def Range(num):
    # R = range(1,11)
    for i in range(1,11):
        if num == i:
            return num,"is present in range"
    return num,"is not present in range"
            
            
print (Range(5))
