'''Q.6 Take two lists and make a dictionary.'''
list1=[1,2,3,4,5,] 
list2=["one","two","three","four","five"]
dict = {}
for i in range(len(list1)-1):
	dict[list1[i]] = list2[i]
print(dict)
