__author__ = 'leihuang'

def safe_division(number, divisor, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number/divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

print safe_division(1.0, 10**500, True, False)
print safe_division(1.0, 0, False, True)

def safe_division(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow',False)
    ignore_zero_division = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' %(kwargs))
    try:
        return number/divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

print safe_division(1.0, 10**500, ignore_overflow = True)
print safe_division(1.0, 0, False, True)
print safe_division(1.0, 0, unexpected = True)