import sys,os
from operation import *
op=Operation(1000,[])
cp=Chip('600230',25,10)
cp1=Chip('600231',10,10)
op.buy(cp)
op.printstat()
op.buy(cp1)
op.printstat()
cp2=Chip('600230',10,5)
op.sell(cp2)
op.printstat()
