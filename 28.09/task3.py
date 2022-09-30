b = {}
while True:
    a = input('Введите место, исполнителя и название трека').split(',')
    if a[0] == 'off':
        break
    b[a[0]+', '+a[1]] = a[2]
    print(b)