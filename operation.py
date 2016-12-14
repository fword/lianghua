class Chip:
    num = 0
    id = ''
    price=0
    shou=0
    value=num*price
    def __init__(self,id='',price=0,num=0):
        self.num=num
        self.price=price
        self.id=id
        self.value=num*price
        self.shou=num/100
class Operation:
    money = 0
    allchips = []
    def __init__(self,money=0,allchips=[]):
        self.money=money
        self.allchips=allchips
    def sell(self,chip):
        tlist=[x.id for x in self.allchips]
        if chip.id not in tlist:
            return 0
        for i in range(len(self.allchips)):
            if self.allchips[i].id==chip.id:
                break
        if chip.num == -1:
            self.allchips = [x for x in self.allchips if not (chip.id==x.id and chip.num<=x.num)]
            self.money+=self.allchips[i].num*chip.price
        elif chip.num<=self.allchips[i].num:
            self.allchips[i].num-=chip.num
            self.money+=self.allchips[i].num*chip.price
        else:
            return 0
        return 1
            
    def buy(self,chip):
        tlist=[x.id for x in self.allchips]
        if chip.value > self.money:
            return 0
        if chip.id not in tlist:
            if chip.num!=-1:
                self.allchips.append(chip)
                self.money -= chip.value
            else:
                shou=self.money//float(100)*chip.price
                if shou<=0:
                    return 0
                chip.shou=shou
                chip.num=100*shou
                chip.value=chip.num*chip.price

                self.allchips.append(chip)
                self.money -= chip.value
        else:
            for i in range(len(self.allchips)):
                if self.allchips[i].id==chip.id:
                    break
            shou=self.money//float(100)*chip.price
            if shou<=0:
                return 0
            chip.shou=shou
            chip.num=100*shou
            chip.value=chip.num*chip.price

            self.allchips[i].num+=chip.num
            self.money -= chip.value
        return 1
            
    def printstat(self):
        print 'left money',self.money
        print 'chips:'
        for item in self.allchips:
            print item.id,item.num,item.price,item.value
                
