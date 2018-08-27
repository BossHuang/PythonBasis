__author__ = 'leihuang'

from threading import Lock
lock = Lock()
with lock:
    print "Lock is held"

lock.acquire()
try:
    print "Lock is held"
finally:
    lock.release()

print "====================="

import logging
def log_func():
    logging.debug("debug one info")
    logging.warning("warning info")
    logging.debug("debug two info")

log_func()

from contextlib import contextmanager
@contextmanager
def debug_looging(leverl):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(leverl)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with debug_looging(logging.DEBUG) as logger:
    print "inside"
    log_func()
    logger.debug("debug inside")
print "outside"
log_func()


