__author__ = 'leihuang'

log = open('logfile', 'w')
url = 'http://www.baidu.com'
print >> log, ('Downloading file from URL %s' % url)
print >> log, 'Files successfully download'