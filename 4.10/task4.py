def IMT():
    ves = int(input('Введите вес - '))
    rost = int(input('Введите рост'))
    imt = rost / (ves *ves)
    return imt


def itog():
    Imt = IMT()
    if Imt < 18.5:
        return print('Недостаточный вес')
    elif Imt <= 18.5 and Imt <25:
        return print('Норма')
    else:
        return print('Большой вес')


itog()