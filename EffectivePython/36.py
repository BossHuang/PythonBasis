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


import os
def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'123456'
    proc = subprocess.Popen(
        ['openssl','enc','-des3','-pass','env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()  # ensure the child gets input
    return proc

procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)

for proc in procs:
    out, err = proc.communicate()
    print out

def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    return proc

input_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc)
    hash_proc = run_md5(proc.stdin)
    hash_procs.append(hash_proc)

for proc in input_procs:
    proc.communicate()
for proc in hash_procs:
    out, err = proc.communicate()
    print out.strip()