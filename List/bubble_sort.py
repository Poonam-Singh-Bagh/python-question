'''Bubble sort flat list'''

new_list = [1, 2, 3, 4, 7, 8, 9, 1, 4, 5, 5, 8, 9, 0, 2, 4, 5, 6, 6, 9]
j=0
while j<len(new_list):
    k=0
    while k<len(new_list)-1:
        if new_list[k] < new_list[k+1]:
            new_list[k],new_list[k+1]=new_list[k],new_list[k+1]
        else:
            new_list[k],new_list[k+1]=new_list[k+1],new_list[k]
        k=k+1
    j=j+1
print (new_list)