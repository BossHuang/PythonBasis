__author__ = 'leihuang'

import time
def factorize(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i
numbers = [212121, 313131, 414141, 515151]
start = time.time()
for number in numbers:
    list(factorize(number))
end = time.time()
print "without multithreading total used %.3f seconds" %(end-start)

from threading import Thread
class FactorizeThread(Thread):
    def __init__(self, number):
        super(FactorizeThread, self).__init__()
        self.number = number
    def run(self):
        self.factors = list(factorize(self.number))

start = time.time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
end = time.time()
print "with multithreading total used %.3f seconds" %(end-start)

print "---------------------"


import time
from threading import Thread
import requests
def get_url_context():
    requests.get("https://www.baidu.com")

start = time.time()
for _ in range(5):
    get_url_context()
end = time.time()
print "without multithreading took %.3f seconds" %(end-start)

start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=get_url_context())
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
end = time.time()
print "with multithreading took %.3f seconds" %(end-start)
