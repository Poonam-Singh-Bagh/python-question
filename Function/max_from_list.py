'''Q.7 Take a list as a parameter and find the maximum number of them'''
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
max = max_num([1,32,55,7,46])
print(max)