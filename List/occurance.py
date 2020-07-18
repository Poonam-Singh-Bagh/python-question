char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
list1=char_list
list2=[]
i=0
while i<len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i=i+1
print (list2)
j=0
list3=[]
while j<len(list2):
    i=0
    count=0
    while i<len(list1):
        if list1[i]==list2[j]:
            count=count+1
        i=i+1
    a=[list2[j],count]
    list3.append(a)
    j=j+1
print (list3
)