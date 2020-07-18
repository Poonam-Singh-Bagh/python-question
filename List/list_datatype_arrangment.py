''' Separate the list by data type wise.'''

list = ["poonam", 78.9, 65, "Rabiya", 87, "Rinki", 37.7, 57]

str_list = []
int_list = []
float_list = []
for i in range(len(list)): 
    if type(list[i]) == str:
        str_list.append(list[i])
    elif type(list[i]) == int:
        int_list.append(list[i])
    elif type(list[i]) == float:
        float_list.append(list[i])
    else:
        print ("Another data type")
print(str_list)
print(int_list)
print(float_list)
    