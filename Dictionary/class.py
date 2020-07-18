'''Classes
Output
{1:[{'Name':'Poonam', 'Roll No.': 7, 'Class': 1},
	{'Name':'Rinki', 'Roll No.': 9, 'Class': 1},
	{'Name':'Rabu', 'Roll No.': 4, 'Class': 1}],
2:[{'Name':'Rabiya', 'Roll No.': 8, 'Class': 2},
	{'Name':'Punnu', 'Roll No.': 3, 'Class': 2}],
3:[{'Name':'Poo', 'Roll No.': 5, 'Class': 3},
	{'Name':'Riku', 'Roll No.': 6, 'Class': 3}]}'''


School = [{'Name':'Poonam', 'Roll No.': 7, 'Class': 1}, 
		{'Name':'Rabiya', 'Roll No.': 8, 'Class': 2},
		{'Name':'Rinki', 'Roll No.': 9, 'Class': 1},
		{'Name':'Punnu', 'Roll No.': 3, 'Class': 2},
		{'Name':'Rabu', 'Roll No.': 4, 'Class': 1},
		{'Name':'Poo', 'Roll No.': 5, 'Class': 3},
		{'Name':'Riku', 'Roll No.': 6, 'Class': 3}]

classes = []
for i in range(len(School)):
	if School[i]['Class'] not in classes:
		classes.append(School[i]['Class'])
dic={}
for j in range(len(classes)):
	list = []
	for k in range(len(School)):
		if classes[j] == School[k]['Class']:
			list.append(School[k])
	dic[classes[j]] = list
			
pprint.pprint(dic)