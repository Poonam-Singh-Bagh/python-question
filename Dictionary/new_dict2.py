''' Make a dictionary where all the dictionaries keys and values 
will be together with update method'''
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
mix_dict = {}
mix_dict.update(dic1)
mix_dict.update(dic2)
mix_dict.update(dic3)
print(mix_dict)
