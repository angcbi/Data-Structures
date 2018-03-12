# -*- coding:utf-8 -*-
import time
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = 1000 * time.time()
        res = func(*args, **kwargs)
        print 'call %s, total cost: %d' % (func.__name__, int(time.time()*1000 - start_time))
        return res
    return wrapper
