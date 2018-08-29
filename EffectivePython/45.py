__author__ = 'leihuang'

from time import localtime, strftime
now = 1407697777
local_tuple = localtime(now)
print local_tuple

time_format = "%Y-%m-%d %H:%M:%S"
time_str = strftime(time_format, local_tuple)
print time_str

from time import mktime, strptime
time_tuple = strptime(time_str, time_format)
print time_tuple

utc_now = mktime(time_tuple)
print utc_now

print "==================================="

from time import strftime, strptime
time_format = "%Y-%m-%d %H:%M:%S"
depart_sfo = "2018-05-01 15:45:16 PDT"
time_tuple = strptime(depart_sfo, time_format)
time_str = strftime(time_format, time_tuple)
print time_str

print "==================================="

import pytz
from datetime import datetime
arrival_nyc = "2018-01-02 10:10:10"
time_format = "%Y-%m-%d %H:%M:%S"
nyc_dt_navie = datetime.strptime(arrival_nyc, time_format)
eastern = pytz.timezone('US/Eastern')
nyc_dt = eastern.localize(nyc_dt_navie)
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
print utc_dt

pacific = pytz.timezone('US/Pacific')
sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
print sf_dt


