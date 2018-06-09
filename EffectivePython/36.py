__author__ = 'leihuang'

import subprocess

proc = subprocess.Popen(
    ['echo', 'Hello World'],
    stdout=subprocess.PIPE
)
out, err = proc.communicate()
print out.decode('utf-8')

proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
    print "working"
    # some time-consuming work heere

print "Exit status", proc.poll()


import time
def run_sleep(period, index):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

start = time.time()
procs = []
for i in range(10):
    proc = run_sleep(0.1, i)
    procs.append(proc)
for proc in procs:
    proc.communicate()
end = time.time()
print "finished in %.3f seconds" %(end-start)