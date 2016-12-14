import sys,os
import urllib,urllib2
from lxml import etree
import socket
import traceback
from bs4 import BeautifulSoup
import time
socket.setdefaulttimeout(5)
def jixxb(content):
    ss=BeautifulSoup(content)
    print ss.find_all('a')
def jixx(content):
    res=[]
    tree=etree.HTML(content)
    try:
        for i in range(2,3):
            for j in range(1260,10000):
                item='//*[@id="quotesearch"]/ul[%d]/li[%d]/a'%(i,j)
                r = tree.xpath(item)
                print item
                if len(r):
                    print r
                    if r[0].text:
                        print r[0].text.encode('utf-8').strip()
    except:
        traceback.print_exc()
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
buf=downurl('http://quote.eastmoney.com/stocklist.html')
#jixxb(buf)
print buf
