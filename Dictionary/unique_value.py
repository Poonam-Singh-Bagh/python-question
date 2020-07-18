'''Q.8 Make a list of unique value.'''
list = [
		{"first":"1"}, 
		{"second": "2"}, 
		{"third": "1"}, 
		{"four": "5"}, 
		{"five":"5"}, 
		{"six":"9"},
		{"seven":"7"}
		]
main_list = []
for i in range(len(list)-1):
	for value in list[i]:
		if list[i][value] not in main_list:
			main_list.append(list[i][value])
print (main_list)

