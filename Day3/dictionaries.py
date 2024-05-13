my_dictionary = {'c1':'value1', 'c2': 'value2'}
print(my_dictionary)

#result = my_dictionary['c1']
print(my_dictionary['c1'])

customer = {"name": 'Barry', 'last_name':'Gawkin', 'weight': 168, 'height':178}

query = (customer['name'])
print(query)


dic = {1:55, 2:[10,20,30],3:{'s1':100, 's2':200}}

print(dic[2][0])
print(dic[3]['s2'])

dic1 = {'k1': ['a','b','c'],'k2':['d','e','f']}
print(dic1['k1']+dic1['k2'])
print(dic1['k2'][1].upper())

dic2 = {1: 'a', 2:'b'}
print(dic2)

dic2[3] = 'c'
print(dic2)
dic2[2] = 'zz'
print(dic2)     #overwrite very simple

print(dic2.keys())
print(dic2.values())
print(dic2.items())