
from novel import *
from novel.scenes import *
#Создание экрана, вывод запроса на имя
titi.hideturtle()
size=103
maint=titi.Turtle()
cl=Click()
maint.hideturtle()
wn = titi.Screen()
wn.setup(1440, 1080)
wn.title('Апокалипис сегодня')
wn.bgpic('bg\\morning1.gif')
name=titi.textinput('Имя', 'Введите имя для главной героини')
last_key=None
character.naming(name)
#Чтение кликов, переключение сцен
def clickOnScreen(x,y):
    titi.hideturtle()
    maint.hideturtle()
    if cl.scenes==0:
        scene1(cl, wn,x,y,character)
    elif cl.scenes==1:
        scene2(cl, wn,x,y,character)
    elif cl.scenes==2:
        scene3(cl, wn, x, y, character)
    elif cl.scenes==3:
        scene4(cl, wn, x, y, character)
    elif cl.scenes==4:
        scene5(cl, wn, x, y, character)
    elif cl.scenes==5:
        scene6(cl, wn, x, y, character)
    elif cl.scenes==6:
        scene7(cl, wn, x, y, character)
    elif cl.scenes==7:
        scene4(cl, wn, x, y, character)
    elif cl.scenes==8:
        scene8(cl,wn, x, y, character)
    elif cl.scenes==9:
        scene5(cl,wn, x, y, character,3)
    elif cl.scenes==10:
        scene6(cl, wn, x, y, character)
    elif cl.scenes==11:
        scene9(cl, wn, x, y, character)
    elif cl.scenes==12:
        scene10(cl, wn, x, y, character)
    cl.clicking1()
    cl.clicking2()
    readChar()
    readInventory()
def RecordKey(key):
    global last_key
    last_key=key
    cl.newButton(key)

widget()
titi.onscreenclick(clickOnScreen)
titi.listen()
titi.onkey(lambda: RecordKey('1'), '1')
titi.onkey(lambda: RecordKey('2'), '2')
titi.onkey(lambda: RecordKey('3'), '3')
titi.onkey(lambda: RecordKey('4'), '4')
titi.onkey(lambda: RecordKey('5'), '5')
titi.onkey(lambda: RecordKey('6'), '6')
titi.onkey(lambda: RecordKey('7'), '7')
titi.onkey(lambda: RecordKey('8'), '8')
titi.onkey(lambda: RecordKey('9'), '9')


wn.mainloop()
