count = 0
with open(input('Введите название исходного файла: '), 'r') as f, open (input('Введите название нового файла: '), 'w+') as g:
    for line in f.readlines():
        count +=1
        g.write(str(count) + ': ' + line)
print('Процесс выполнен!')