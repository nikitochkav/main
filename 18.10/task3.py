import random
Count_1 = 1
a = []
b = []
print('Учасники Соревнования')
while True:
    Sluch = random.randint(1, 3)
    if Sluch == 1:
        num_1 = input('Учасник команды №1 - ')
        if num_1 == "off":
            break
        else:
            print('Ваш номер -', Count_1)
            a.append(num_1)
            Count_1 +=1
    else:
        num_2 = input('Учасник команды №2 - ')
        if num_2 == "off":
            break
        else:
            b.append(num_2)
            print('Ваш номер -', Count_1)
            a.append(num_2)
            Count_1 +=1

print('Список учасников готов')
print('Команда 1 -', a)
print('Команда 2 -', b)