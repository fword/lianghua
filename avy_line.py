import sys,os
n=int(sys.argv[1])
ol=[]
for line in sys.stdin:
    line=line.strip()
    ol.append(line)
ol.pop(0)
ol.reverse()
nl=[]
pre=[]
for item in ol:
    #cur=item.split(',')[1:]
    liang=item.split(',')[-2].strip()
    if liang=='000':
        continue
    else:
        nl.append(item)
    #pre=cur
ajust=[float(line.split(',')[-1].strip()) for line in nl]
for i in range(len(nl)):
    if i<n:
        start=1
    else:
        start=i-n+1
    avg=sum(ajust[start:i+1])/float(n)
    print nl[i]+','+str(avg)
    
