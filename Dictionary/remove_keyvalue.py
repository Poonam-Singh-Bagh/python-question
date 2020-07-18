'''Q.5 Remove ('A' : 'WELCOME') from the dictionary.'''
Dic= {
	1: 'NAVGURUKUL',
	2: 'IN', 
	3: { 
		'A' : 'WELCOME',
		'B' : 'To',
		'C' : 'DHARAMSALA'
		}
	}
del (Dic[3]['A'])
print (Dic)
