'''Q.7 Take two list as a parameter and find the maximum number of them'''
def max_num(list):
    i=0
    max=list[0]
    while i<len(list):
        if max < list[i]:
            max=list[i]
        else:
            max=max
        i=i+1
    return max
    
def main_fun(list1,list2):
    max1 = max_num(list1)
    max2 = max_num(list2)
    if max1 > max2:
        return "max1 is greater", max1
    else:
         return "max2 is greater", max2

list1 = [34,45,56,67]
list2 = [33,56,34,23]
print(main_fun(list1,list2))

