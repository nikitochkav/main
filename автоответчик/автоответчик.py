print('Добро пожаловать в спортивный комплекс "Олимп"')
print('Введите, что вам нужно')
while True:
    def schedule():
        return '08:00 - Бассейн\n09:00 - Баскетбол\n21:00 - Футбол\n22:00 - Волейбол'
    def couch():
        a = int(input('Выберите тренера (введите номер):\n1. Василий Анатольевич\n2. Константин Игорввич\n3. Пётр Александрович\n4. Дмитрий Алексеевич\n'))
        d = {
            1:['Василий Анатольевич', '+79263546788'],
            2:['Константин Игоревич', '+79263646089'],
            3:['Пётр Александрович', '+79233546789'],
            4:['Дмитрий Алексеевич', '+79234560987']
        }
        return '\n'.join(d[a])
    def oplata():
        return int(input('Сколько вы посетили занятий? '))*350

    def address():
        return 'город Лабинск, улица Лермонтова, 79'
    def site():
        return 'https://www.mobu-olimp.ru'
    a = input()
    if 'расп' in a:
        print(schedule())
    elif 'трен' in a:
        print(couch())
    elif 'плат' in a:
        print(oplata())
    elif 'адр' in a:
        print(address())
    elif 'сайт' in a:
        print(site())