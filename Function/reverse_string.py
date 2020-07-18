'''Q 4. Write a Python program to reverse a string.'''
def reverse_string(string):           #def reverse_string(string):
    # string = "1234abcd"             #rev_str = " "
    rev_str = " "                     # i=len(string)-1
    i=len(string)-1                   #for i in range(i,-1,-1):
    while i > -1:                     #     rev_str += string[i]
        rev_str += string[i]          #return (rev_str)
        i=i-1
    return (rev_str)


print (reverse_string("1234abcd"))  #Caliing the function.

