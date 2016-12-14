import sys,os
import urllib,urllib2
from lxml import etree
import socket
import traceback
from bs4 import BeautifulSoup
import time
socket.setdefaulttimeout(5)
def downurl(tarurl):
    for i in range(3):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML,         like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
            req = urllib2.Request(url=tarurl,headers=headers)
            content =urllib2.urlopen(req, timeout=5).read()
            return content
        except:
            traceback.print_exc()
            pass
for line in sys.stdin:
    line=line.strip()
    pre=line[:2]
    pos=line[2:]
    if pre=='sh':
        tar=pos+'.'+'ss'
    else:
        tar=pos+'.'+'sz'
    buf=downurl('http://table.finance.yahoo.com/table.csv?s=%s'%tar)
    if buf:
        ff=open('data/%s'%line,'w+')
        ff.write(buf)
        ff.close()
    
