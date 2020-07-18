'''Bubble sort of nested list (Interview)'''
list = [[8,7,4,9,3,1,2],[5,1,8,9,4,5],[2,6,9,5,4,6,0]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        k=0
        while k<len(list[i])-1:
            if list[i][k] < list[i][k+1]:
                list[i][k],list[i][k+1]=list[i][k],list[i][k+1]
            else:
                list[i][k],list[i][k+1]=list[i][k+1],list[i][k]
            k=k+1
        j=j+1
    i=i+1
print (list)