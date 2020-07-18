'''Sorting of the list'''

list=[10,5,3,20,2,1]
for index in range(1,len(list)):
    value = list[index]
    i=index-1
    while i>=0:
        if value < list[i]:
            list[i+1]=list[i]
            list[i]=value
            i=i-1
        else:
            break
print(list)
        
      
