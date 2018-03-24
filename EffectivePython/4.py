__author__ = 'leihuang'

# python3
from urllib.parse import parse_qs
value = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(value)

print('Red: ',value.get('red'))
print('Green: ',value.get('green'))
print('Yellow: ',value.get('yellow'))

red = value.get('red', [''])[0] or 0
print(red)

def get_first_int(value, key, default=0):
    result = default
    found = value.get(key, [''])
    if found[0]:
        result = int(found[0])
    return result
