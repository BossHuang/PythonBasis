__author__ = 'leihuang'

import os
os.system('ls')

result = os.popen('ls')
print result
print result.read()

import commands
print [x for x in dir(commands) if not x.startswith("__")]

status, result = commands.getstatusoutput('ls')
print status
print result

import subprocess
subprocess.call(['ls'])
subprocess.check_call(['ls'])
result = subprocess.check_output(['ls'])
print result
