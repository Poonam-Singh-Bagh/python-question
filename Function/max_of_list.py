'''Q.7 with one loop and two run two different for each list.'''
def max_num(list1,list2):
    i=0
    max1=list1[0]
    while i<len(list1):
        if max1 < list1[i]:
            max1=list1[i]
        else:
            max1=max1
        i=i+1
        
    i=0
    max2=list2[0]
    while i<len(list2):
        if max2 < list2[i]:
            max2=list2[i]
        else:
            max2=max2
        i=i+1
    if max1 < max2:
        return max2
    else:
        return max1

max = max_num([4,3,5,2],[6,7,8,4])
print (max)
    