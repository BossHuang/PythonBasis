__author__ = 'leihuang'

import re

line = "Hello, my name is Ben.Please visit my Website at http://www.forta.com/."
line2 = "The phrase \"regular expression\" is often abbreviated as RegEx or regex."
nameDocuments = """sales.xls
          sales1.xls
          orders3.xls
          sales2.xls
          sales3.xls
          apac1.xls
          europe2.xls
          na1.xls
          na2.xls
          sa1.xls
          usa1.xls
          sam.xls"""
#matchObj = re.match(r'my',line)
#if matchObj:
 #   print "matchObj.group : ", matchObj.group()
#else:
  #  print "No Match"

searchObj = re.search(r'my',line)
if searchObj:
    print "my : ", searchObj.group()
else:
    print "my NO FOUND"

searchObj = re.search(r'hello',line)
if searchObj:
    print "hello : ", searchObj.group()
else:
    print "hello NO FOUND"

searchObj = re.search(r'B.',line)
if searchObj:
    print "B. : ", searchObj.group()
else:
    print "B. NO FOUND"

searchObj = re.search(r'\/ww.\.',line)
if searchObj:
    print "\/ww.\. : ",searchObj.group()
else:
    print "\/ww.\. NO FOUND"

searchObj = re.search(r'[ns]a.\.xls',nameDocuments)
if searchObj:
    print "[ns]a.\.xls : ",searchObj.group();
else:
    print "No found. [ns]a.\.xls"

searchObj = re.search(r'[Rr]eg[Ee]x',line2)
if searchObj:
    print "[Rr]eg[Ee]x : ",searchObj.group()
else:
    print "[Rr]eg[Ee]x NO FOUND"

searchObj = re.search(r'[ns]a[0-9]\.xls',nameDocuments)
if searchObj:
    print "[ns]a[0-9]\.xls : ",searchObj.group()
else:
    print "[ns]a[0-9]\.xls NO FOUND"

searchObj = re.search(r'[A-Z0-9a-z]a',nameDocuments)
if searchObj:
    print "[A-Z0-9a-z]a : ",searchObj.group()
else:
    print "[A-Z0-9a-z]a NO FOUND"

searchObj = re.search(r'[ns]a[^0-9]\.xls',nameDocuments)
if searchObj:
    print "[ns]a[^0-9]\.xls", searchObj.group()
else:
    print "[ns]a[^0-9]\.xls NO FOUND"