from queue import Queue

from threading import Thread
import threading

import time

# Shared Memory variables
CAPACITY = 10
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0

# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)


def producer(name):

    """Productor"""
    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full
    items_produced = 0
    counter = 0

    while items_produced < 20:
        empty.acquire()
        mutex.acquire()

        counter += 1
        buffer[in_index] = counter
        in_index = (in_index + 1)%CAPACITY
        print(f"{name} está produciendo el bollo {counter}")
        mutex.release()
        full.release()

        time.sleep(1)

        items_produced += 1

def customer(name):

    """consumidor"""

    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full

    items_consumed = 0

    while items_consumed < 20:
        full.acquire()
        mutex.acquire()

        item = buffer[out_index]
        out_index = (out_index + 1)%CAPACITY

        print(f"El consumidor- {name} está comiendo el bollo {item}")
        mutex.release()
        empty.release()

        time.sleep(1)
        items_consumed += 1


if __name__ == '__main__':

    t1 = Thread(target=producer,args=("Maestro Zhang",))

    t2 = Thread(target=customer,args=("Xiaoming",))

    t1.start()

    t2.start()

