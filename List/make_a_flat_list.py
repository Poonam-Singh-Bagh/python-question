'''Sort the nested list and make it flat list'''

list = [[8,7,4,9,3,1,2],[5,1,8,9,4,5],[2,6,9,5,4,6,0]]
new_list = []
i=0
while i<len(list):
    new_list.extend(list[i])
    i=i+1    
a=0
while a<len(new_list):
    b=0
    while b<len(new_list)-1:
        if new_list[b] < new_list[b+1]:
            new_list[b],new_list[b+1]=new_list[b],new_list[b+1]
        else:
            new_list[b],new_list[b+1]=new_list[b+1],new_list[b]
        b=b+1
    a=a+1
print(new_list)