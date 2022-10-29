import time
while True:
    a = input('Удалить с поля?(да/нет)')
    if a == 'нет':
        break
    elif a == 'да':
        b = int(input('Введите кол-во минут: '))
        print('Вы удалены с поля на', str(b), 'минут(ы)')
        time.sleep(b)
        print('Вернитесь на поле!')
    else:
        print('Попробуйте еще раз')