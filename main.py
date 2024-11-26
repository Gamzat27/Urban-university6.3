my_dict = {'qqq':111,'www':222,'eee':333}
print(my_dict)
print(my_dict['qqq'])
my_dict['rrr'] = 444
print(my_dict)
my_dict.update({'ttt':555,'yyy':666})
print(my_dict)
print(my_dict['qqq'])
print(my_dict.get('qqq'))
del my_dict['qqq']
a = my_dict.pop('eee')
print(a)
print(my_dict.get('qqq'))
print(my_dict)

my_set = {1,2,3,1,2,3,'string',True,'aaa'}
print(my_set)
print(my_set.add(9))
print(my_set.add(7))
print(my_set)
print(my_set.discard(7))
print(my_set)


