list1 = {}
list1['1'] = 1
list1['2'] = 2
list1['3'] = 3
list1['5'] = 5
list1['6'] = 6

print(list1)

element1 = list1.get('1')
element6 = list1.get('6')

list1['1'] = element6
list1['6'] = element1

list1['new_key'] = 'new_value'
print(list1)
