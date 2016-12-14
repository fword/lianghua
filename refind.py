import sys,os
import re
for line in sys.stdin:
    line=line.strip()
    ret=re.findall("http\:\/\/quote\.eastmoney\.com\/(.*)\.html",line)
    for item in ret:
        print item


