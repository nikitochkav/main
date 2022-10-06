def print_name():
    x = input('Имя - ')
    y = input('Группа - ')
    print(x, y)


children = int(input('Число учеников'))
for i in range(children):
    print_name()
print('Готово')