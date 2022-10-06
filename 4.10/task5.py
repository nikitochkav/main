def nagrada():
    ball = sum(colvo)
    if ball > 50 and ball <= 80:
        print('Наградить похвальной грамотой.')
    elif ball > 80:
        print('Наградить дипломом.')
    else:
        print('Выдать грамоту об участии.')


def sum(colvo):
    x = 0
    for i in range(colvo):
        ball = int(input('Введите баллы по предмету: '))
        x = x+ball
    print('Итоговый счёт: ',x)
    return x

x = 0
while x != 'off':
    name = input('Введите имя: ')
    if name == 'off':
        x = name
        break
    colvo = input('Введите кол-во предметов: ')
    if colvo == 'off':
        x = colvo
        break
    else:
        colvo = int(colvo)
    nagrada()


print('Ты возможно молодец')