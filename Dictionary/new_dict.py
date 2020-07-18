'''Q.2 Make a dictionary where all the dictionaries keys and values will be together'''
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
mix_dict = {}
for key, value in dic1.items():
	mix_dict[key]=dic1[key]
for key, value in dic2.items():
	mix_dict[key]=dic2[key]
for key, value in dic3.items():
	mix_dict[key]=dic3[key]
print(mix_dict)

