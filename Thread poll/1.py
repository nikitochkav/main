from queue import Queue
from threading import Thread
from time import sleep

import sys


x = 0
def dobavlenie(queue, x):
    if type(x) == str:
        queue.put(x)


def otchislenie(queue):
     while True:
         try:
             item = queue.get()
             print(f'Студент {item} отчислен')
         except:
             ...

queue = Queue()
for i in ('Петров', "Иванов"):
    queue.put(i)


while x != 'off':
    thread1 = Thread(target=dobavlenie, args={queue, x})
    thread1.start()
    thread1.join()

    thread2 = Thread(target=otchislenie, args={queue, }, daemon=True)
    thread2.start()

    sleep(1)
    x = input('введите фамилию студента: ')


