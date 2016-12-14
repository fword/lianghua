import sys
cnt=0
idx=0
allm=10000
ol=[]
bf=0
sf=1
buynum=0
leva=0
cishu=int(sys.argv[1])
def buy(allm,num):
    gushu=allm//num
    shou=gushu//100
    leva=allm-shou*100*num
    return shou,leva
def sell(num,bug):
    return num*bug*100
for line in sys.stdin:
    line=line.strip()
    idx+=1
    avg=float(line.split(',')[-1].strip())
    num=float(line.split(',')[-2].strip())
    dat=line.split(',')[0]
    if num>=avg:
        cnt+=1
        if cnt>=cishu:
            if sf==1 and bf==0:
                buynum,leva=buy(allm,num)
                print 'buy',buynum,'at',num,dat,'allmoney',allm
                bf=1
                sf=0
    else:
        if cnt:
            ol.append(cnt)
        cnt=0
        if bf==1 and sf==0:
            rets=sell(num,buynum)
            print 'sell',buynum,'at',num,dat,'allmoney',allm
            #print num,buynum,rets
            allm=rets+leva
            sf=1
            bf=0
            buynum=0
print allm
