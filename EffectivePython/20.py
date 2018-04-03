__author__ = 'leihuang'

from datetime import datetime
import time
def log(message, when=datetime.now()):
    print "%s: %s" %(when, message)

log('hi')
time.sleep(1)
log('hi again')

import json
def decode(data, default = {}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode("bad data")
foo['s'] = 1
bar = decode("bad data again")
bar['a'] = 2

print foo
print bar

from datetime import datetime
import time
def log(message, when=None):
    '''
    Log a message with a timestamp
    :param message: message to print
    :param when: datetime of when the message occurred.
            Defaults to the present time.
    :return:
    '''
    when = datetime.now() if when is None else when
    print "%s: %s" %(when, message)

log('hi')
time.sleep(1)
log('hi again')