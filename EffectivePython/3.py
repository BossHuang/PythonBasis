__author__ = 'leihuang'

# Python2
def to_unicode(unicode_or_str):
    value = unicode_or_str
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    return value

def to_str(unicode_or_str):
    value = unicode_or_str
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    return value

s = '123'
print type(s)
a = to_unicode(s)
print type(a)


