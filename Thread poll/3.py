import os
from queue import Queue
from threading import Thread

queue = Queue()


def name(queue):
    x = os.getcwdb()
    count = 0
    with open("Name.txt", "r") as f:
        for i in f.readlines():
            y = i.replace("\n", "")
            os.mkdir(y)
            y = x.decode() + "\\" + y + "\\" + y + ".txt"
            print(y)
            queue.put(y)


def create(queue):
    while not queue.empty():
        x = queue.get()
        with open(f"{x}", "w+") as f:
            pass



th1 = Thread(target=name, args=(queue,))
th1.start()
th1.join()
th2 = Thread(target=create, args=(queue,))
th2.start()
