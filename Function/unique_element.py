'''Q 8. Write a Python function that takes a list and returns a new list 
with unique elements of the first list.'''

def simple_list(list):
    unique_list = []
    i=0
    while i < len(list):
        if list[i] not in unique_list:
            unique_list.append(list[i])
        i+=1
    return unique_list
    
print (simple_list([1,2,3,3,3,3,4,5]))
