'''Q.2 Make list where each list has 10 elements.'''

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
i=0
while(i<len(list)):
    list1=[]
    j=i
    while(j<i+5):
        list1.append(list[j])
        j+=1
    print(list1)
    i+=5