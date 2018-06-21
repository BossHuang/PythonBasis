__author__ = 'leihuang'

import thread
from time import sleep,ctime

loops = [4,2]

def loop(nloop, nsec, lock):
    print "start loop ", nloop, 'at:', ctime()
    sleep(nsec)
    print "end loop ", nloop, 'at:', ctime()
    lock.release()

def main():
    print "starting at:", ctime()
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = thread.allocate()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    print "ending at:", ctime()

if __name__ == '__main__':
    main()

print "--------------------"

from threading import Thread
from time import sleep,ctime

loops = [4,2]

def loop_thread_v1(nloop, nsec):
    print "start loop ", nloop, 'at:', ctime()
    sleep(nsec)
    print "end loop ", nloop, 'at:', ctime()

def main_thread_v1():
    print "starting at:", ctime()
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = Thread(target=loop_thread_v1, args=(i, loops[i]))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print "ending at:", ctime()

if __name__ == '__main__':
    main_thread_v1()

print "--------------------"


from threading import Thread
from time import sleep,ctime

loops = [4,2]

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args
    def __call__(self):
        self.func(*self.args)

def loop_thread_v1(nloop, nsec):
    print "start loop ", nloop, 'at:', ctime()
    sleep(nsec)
    print "end loop ", nloop, 'at:', ctime()

def main_thread_v2():
    print "starting at:", ctime()
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = Thread(target=ThreadFunc(loop_thread_v1, (i, loops[i]), loop_thread_v1.__name__))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print "ending at:", ctime()

if __name__ == '__main__':
    main_thread_v2()

print "--------------------"

from threading import Thread
from time import sleep,ctime

loops = [4,2]

class MyThread(Thread):
    def __init__(self, func, args, name=''):
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        self.func(*self.args)

def loop_thread_v1(nloop, nsec):
    print "start loop ", nloop, 'at:', ctime()
    sleep(nsec)
    print "end loop ", nloop, 'at:', ctime()

def main_thread_v3():
    print "starting at:", ctime()
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop_thread_v1, (i, loops[i]), loop_thread_v1.__name__)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print "ending at:", ctime()

if __name__ == '__main__':
    main_thread_v3()

