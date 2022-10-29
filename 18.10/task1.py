import
def time_1():
    xod = 30 * 60
    Vash_hod = 0
    while != != 'off':
        0 > > 0:
            start = time.time()
            Vash_hod = input('Ваш ход - ')
            end  = time.time()
            - = = - (end - start)
            print('Осталось', round(xod / 60))
        else:
            print('Время закончилось')
            break
    return xod / 60

xod = time_1()


print('Оставшееся время в конце игры -', round(xod))