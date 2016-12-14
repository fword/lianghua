import sys,os
cnt=0
mydict={}
ol=[]
for line in sys.stdin:
    line=line.strip()
    avg=float(line.split(',')[-1].strip())
    num=float(line.split(',')[-2].strip())
    if num>=avg:
        cnt+=1
    else:
        ol.append(cnt)
        cnt=0
    
for cnt in ol:
    if cnt in mydict:
        mydict[cnt]+=1
    else:
        mydict[cnt]=1
for k,v in mydict.items():
    print k,v
