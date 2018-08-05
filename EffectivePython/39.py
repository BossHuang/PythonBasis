__author__ = 'leihuang'

from collections import deque
from threading import Lock
from threading import Thread
from time import sleep

class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()
    def put(self, item):
        with self.lock:
            self.items.append(item)
    def get(self):
        with self.lock:
            return self.items.popleft()

class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super(Worker, self).__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0
    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                sleep(0.1)
            else:
                result = self.func(item)
                self.out_queue.put(item)
                self.work_done += 1

def download(item):
    pass

def resize(item):
    pass

def upload(item):
    pass

download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue)
]

for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())

while len(done_queue.items) < 1000:
    pass

if len(done_queue.items) >= 1000:
    print "done"

processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print "processed %d, items after polling polled %d times" %(processed, polled)

print "=================="

from Queue import Queue
from threading import Thread
from time import sleep
queue = Queue(1)
def consumer():
    print "Consumer waiting"
    sleep(0.1)
    queue.get()
    print "consumer get 1"
    queue.get()
    print "consumer get 2"
    print "Consumer done"
    queue.task_done()

thread = Thread(target=consumer)
thread.start()

print "Producter puting"
queue.put(object())
print "producter put 1"
queue.put(object())
print "producter put 2"
thread.join()
print "Producter done"

print "==========="

from Queue import Queue
from threading import Thread
class ClosableQueue(Queue):
    SENTINEL = object()
    def close(self):
        self.put(self.SENTINEL)
    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()

class StoppableWorker(Thread):
    def __init__(self,func, in_queue, out_queue):
        super(StoppableWorker, self).__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0
    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(item)

def download(item):
    pass

def resize(item):
    pass

def upload(item):
    pass

download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()
threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue)
]

for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())
download_queue.close()
download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print done_queue.qsize()
