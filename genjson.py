#coding=utf-8
import sys,os
from lxml import etree
import dluse
import html2text
import json
reload(sys)
sys.setdefaultencoding('utf-8')
item='/html/body/table/tr[%d]/td[%d]/span'
path=sys.argv[1]
baogao=['ss','16-09-30','16-06-30','16-03-31','15-12-31','15-09-30','15-06-30','15-03-31','14-12-31','14-09-30']
namelst=[]
for line in os.listdir(path):
    filename=os.path.join(path,line)
    idres={}
    idres[line]=[]
    buf=open(filename).read()
    if buf:
        tree=etree.HTML(buf)
        for j in range(1,11):
            timelst={}
            timelst[baogao[j-1]]=[]
            for i in range(1,100):
                r = tree.xpath(item%(i,j))
                if len(r):
                    value=r[0].text
                else:
                    continue
                if j==1:
                    #namelst.append(value)
                    namelst.append('eps')
                    #print len(namelst)
                else:
                    if i-1 >= len(namelst):
                        continue
                    name=namelst[i-1]
                    tmp={}
                    tmp[name]=value
                    timelst[baogao[j-1]].append(tmp)
            idres[line].append(timelst)
        print json.dumps(idres)
