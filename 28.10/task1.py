a = 0
while a != 'off':
    a = input('Введите имя - ')
    b = lambda a:\
        a + ' гений'
    print(b(a))