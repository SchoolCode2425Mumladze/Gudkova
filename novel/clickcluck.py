#Счетчик
class Click:
    click=0
    click2=0
    scenes=0
    button=None
    def clicking1(self):
        self.click+=1
    def clicking2(self):
        self.click2 += 1
    def endScene(self):
        self.scenes+=1
    def noClick(self):
        self.click=0
    def newButton(self,button):
        self.button=button
#Определение того, какой выбор сделал игрок
def whichChoice(x,y):
    if -555<=x<=532 and -240<=y<=-220:
        return 1
    elif -555<=x<=532 and -330<=y<=-310:
        return 2
    else:
        return 0
def whichChar3(x,y):
    if -555<=x<=532 and -240<=y<=-220:
        return 1
    elif -555<=x<=532 and -280<=y<=-260:
        return 2
    elif -555<=x<=532 and -320<=y<=-300:
        return 3
    else:
        return 0
def WhichItem(x,y):
    #1=fl,2=med,3=fb,4=mm,5=exit
    if -462<=x<=-291 and 50<=y<=244:
        return 1
    elif -151<=x<=0 and 54<=y<=237:
        return 2
    elif 155<=x<=300 and 72<=y<=230:
        return 3
    elif -453<=x<=-300 and -167<=y<=-95:
        return 4
    elif -120<=x<=31 and -200<=y<=-69:
        return 5
    else:
        return 1000
class Choise:
    cmd2=0
    def __init__(self,command,):
        self.command=command
