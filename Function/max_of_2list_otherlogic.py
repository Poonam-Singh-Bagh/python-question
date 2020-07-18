''' Q.7 With one function with combined two list together.'''
def max_num(list1,list2):
    list1.extend(list2)
    i=0
    max=list1[0]
    while i<len(list1):
        if max < list1[i]:
            max=list1[i]
        else:
            max=max
        i=i+1
    return max
    
    
max_number = max_num([4,3,5,2],[6,7,8,4])
print (max_number) 
    
