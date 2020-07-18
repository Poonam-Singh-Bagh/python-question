'''Q 7. Write a Python function that accepts a string and calculate the 
number of upper case letters and lower case letters.''' 

def String(str):
    UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    UPPER = 0
    lower = 0
    for i in str:
        if i in UPPER_CASE:
            UPPER += 1
        elif i in lower_case:
            lower += 1
    return UPPER, lower


UPPER, lower = String('The quick Brow Fox')
print ("No. of Upper case characters :", UPPER)
print ("No. of Upper case characters :", lower)   
