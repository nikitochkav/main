grades = [{'name': 'Vasya', 'final': 99},
     {'name': 'Misha', 'final': 123},
    {'name': 'Kostya', 'final': 1}]

new_list = (sorted(grades, key=lambda x:x['name']))
print(new_list)