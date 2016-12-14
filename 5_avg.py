import sys,os
al=[]
for line in sys.stdin:
    line=line.strip()
    al.append(line)
al.pop(0)
al.reverse()
bn=[]
for line in al:
    mylist=line.split(',')
    try:
        avg5=sum(bn)/float(5)
        num=float(mylist[-1])
        if len(bn)>=5 
            if num>=agv5:
                res.append(num)
            else:
                res=[]
        if len(bn)<5:
            bn.append(line)
        else:
            bn.pop(0)
            bn.append(num)
        #avg5=avg([float(item.split(',')[-1]) for item in bn])
    except:
        continue

