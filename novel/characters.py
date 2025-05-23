import turtle as tu
import random

myColor='#d99a6c'
class MainCharacter:
    name='Жаклин'
    colour='#f4cfcf'
    inventory=[]
    dexterity=random.randint(0,5)
    strength=random.randint(0,5)
    intelegence=random.randint(0,5)
    balance = 0
    new_balance=0
    cc=1111111
    ending=0
    def naming(self,new_name):
        if type(new_name)!=type(None):
            if new_name!='':
                self.name=new_name
    def getNewItem(self,item):
        self.inventory.append(item)
character=MainCharacter()
class Valerin:
    favorites=['Книга', 'Сладости',"Закладка"]
    name='Валерин'
    age=21
    sprite = 'sprites\валерин.gif'
    rep=0
    wcolour='#97b1ce'
    valerin_shape = tu.Turtle()
    valerin_shape.hideturtle()
    def createSpriteValerin(self, wn):
        self.valerin_shape.showturtle()
        wn.addshape(self.sprite)
        self.valerin_shape.shape(self.sprite)
    def hideValerin(self):
        self.valerin_shape.hideturtle()
    def showValerin(self):
        self.valerin_shape.showturtle()
valerinC=Valerin()
class Arashi:
    favorites=['Сладости','Вышивка','Медиатор']
    name='Араши'
    age=19
    sprite = 'sprites\араши.gif'
    rep=0
    mcName=None
    wcolour='#c4b1d2'
    arashi_shape = tu.Turtle()
    arashi_shape.hideturtle()
    def createSpriteArashi(self, wn):
        self.arashi_shape.showturtle()
        wn.addshape(self.sprite)
        self.arashi_shape.shape(self.sprite)
    def hideArashi(self):
        self.arashi_shape.hideturtle()
    def showArashi(self):
        self.arashi_shape.showturtle()
Arashic=Arashi()
class Cloe:
    name='Хлоя'
    age=18
    sprite='sprites\хлоя.gif'
    favorites = ['Сладости', 'Красный мяч','Цветок']
    rep=0
    cloe_shape = tu.Turtle()
    cloe_shape.hideturtle()
    wcolour = '#c0e8d7'
    def createSpriteCloe(self, wn):
        self.cloe_shape.showturtle()
        wn.addshape(self.sprite)
        self.cloe_shape.shape(self.sprite)
    def hideCloe(self):
        self.cloe_shape.hideturtle()
    def showCloe(self):
        self.cloe_shape.showturtle()
Cloec=Cloe()
class Dad:
    dad_shape=tu.Turtle()
    dad_shape.hideturtle()
    sprite = 'sprites\отец.gif'
    rep=100
    wcolour='#b0a7a7'
    def createSpriteDad(self,wn):
        self.dad_shape.showturtle()
        wn.addshape(self.sprite)
        self.dad_shape.shape(self.sprite)
    def hideDad(self):
        self.dad_shape.hideturtle()
    def showDad(self):
        self.dad_shape.showturtle()
daddy=Dad()
class Kitten:
    kitten_shape=tu.Turtle()
    kitten_shape.hideturtle()
    sprite ='sprites//Луна.gif'
    rep=-2
    wcolor='#d2d0b1'
    def createSpriteCat(self,wn):
        self.kitten_shape.showturtle()
        wn.addshape(self.sprite)
        self.kitten_shape.shape(self.sprite)
    def hideCat(self):
        self.kitten_shape.hideturtle()
    def showCat(self):
        self.kitten_shape.showturtle()
kitten=Kitten()
mc=character

class Vernon:
    name='Вернон'
    age=15
    sprite = 'sprites\вернон.gif'
    rep=40
    wcolour='#ceb497'
    vernon_shape = tu.Turtle()
    vernon_shape.hideturtle()
    def createSpriteVernon(self, wn):
        self.vernon_shape.showturtle()
        wn.addshape(self.sprite)
        self.vernon_shape.shape(self.sprite)
    def hideVernon(self):
        self.vernon_shape.hideturtle()
    def showVernon(self):
        self.vernon_shape.showturtle()
vernon=Vernon()
#Чтение характеристик и вывод
def readChar(cmd=False):

    if cmd:
        with open('info\\mc info.txt', 'r') as f:
            tr = []
            for i in range(4):
                to_add = f.readline()
                tr.append(to_add.strip())
            f.close()
            return tr
    else:
        with open('info\\mc info.txt', 'w') as f:
            f.write(f'Ловкость:{mc.dexterity}\n')
            f.write(f'Сила:{mc.strength}\n')
            f.write(f'Интеллект:{mc.intelegence}\n')
            f.write(f'Баланс:{mc.balance}\n')
            f.close()
#Чтение инвентаря и вывод
def readInventory(cmd=False):
    ch=1
    if cmd:
        with open('info\\inventory.txt', 'r') as f:
            ni=[]
            for i in range(3):
                to_add=f.readline()
                if to_add!='':
                    ni.append(to_add.strip())
            f.close()
        return ni
    else:
        with open('info\\inventory.txt', 'w') as f:
            inventory=mc.inventory
            for i in inventory:
                f.write(f'{ch}.{i}\n')
                ch+=1
        f.close()
class zzz:
    statToBeat=random.randint(1,7)
    zombie = tu.Turtle()
    zombie.hideturtle()
    zombie.up()
    def createZombie(self,wn):
        self.zombie.up()
        self.zombie.goto(-100, -150)
        wn.addshape('sprites\\zombie.gif')
        self.zombie.shape('sprites\\zombie.gif')
        self.zombie.showturtle()
    def hidezzz(self):
        self.zombie.hideturtle()
    def updateStat(self):
        self.statToBeat=random.randint(1,10)
zombie=zzz()