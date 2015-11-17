import threading
from time import sleep
import os

state = [''] * 5
mutex = threading.Lock()
philosophers = [''] * 5

class Philosopher(threading.Thread):
    EATING = 'EATING'
    HUNGRY = 'HUNGRY'
    THINKING = 'THINKING'

    def __init__(self, i):
        threading.Thread.__init__(self)
        self.name = 'P' + str(i)
        self.i = i
        self.cond = threading.Condition()

    def run(self):
        while True:
            self.cond.acquire()
            mutex.acquire()
            state[self.i] = Philosopher.HUNGRY
            if state[self.i] != Philosopher.EATING:
                if all(map(lambda x: x == Philosopher.HUNGRY, state)):
                    self.ask(self.i - 1)
                mutex.release()
                self.cond.wait()
            else:
                mutex.release()

            print (self.name + ' is eating!')
            sleep(1)

            mutex.acquire()
            state[self.i] = Philosopher.EATING
            self.ask(self.i - 1)
            mutex.release()
            print (self.name + ' is thinking!')
            self.cond.release()

    def ask(self, j):
        if state[(j - 1) % 5] != Philosopher.EATING and \
            state[(j + 1) % 5] != Philosopher.EATING and \
            state[j] == Philosopher.HUNGRY:
            philosophers[j].cond.acquire()
            state[j] = Philosopher.EATING
            philosophers[j].cond.notify()
            philosophers[j].cond.release()


if __name__ == '__main__':
    philosophers = [Philosopher(i) for i in range(5)]
    for p in philosophers:
        print (p)
        p.start()
    # Allow CTRL + C to exit the program
    try:
        while True:
            sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)
