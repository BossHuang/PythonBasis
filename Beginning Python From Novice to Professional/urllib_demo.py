__author__ = 'leihuang'

from urllib import urlopen
import  re
webpage = urlopen("https://www.baidu.com")
text = webpage.read()
print len(text)
p = r'(http(s){0,1}://)?www\.[0-9a-zA-Z]+\.com'
m = re.search(p, text, re.IGNORECASE)
print m.group()