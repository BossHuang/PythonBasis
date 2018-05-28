__author__ = 'leihuang'

import datetime
'''
class Bucket(object):
    def __init__(self, period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.quota = 0

    def __repr__(self):
        return 'Bucket(quota=%d)' % self.quota
'''
def fill(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount

def deduct(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        print "Not enough for %d qouta" % amount
        return False
    bucket.quota -= amount
    print "Had %d qouta" % amount
    return True




class Bucket(object):
    def __init__(self, period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.init_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return ('Bucket(init_quota=%d, quota_consumed=%d)' %(self.init_quota, self.quota_consumed))

    @property
    def quota(self):
        return self.init_quota - self.quota_consumed
    @quota.setter
    def quota(self, amount):
        print amount
        delta = self.init_quota - amount
        if amount == 0:
            # Quota being reset for a new period
            self.quota_consumed = 0
            self.init_quota = 0
        elif delta < 0:
            # Quota being filled for the new period
            assert self.quota_consumed == 0
            self.init_quota = amount
        else:
            # Quota being consumed during the period
            assert self.init_quota >= self.quota_consumed
            self.quota_consumed += delta


bucket = Bucket(60)
fill(bucket, 100)
print bucket
deduct(bucket, 99)
print bucket
deduct(bucket, 3)
print bucket
