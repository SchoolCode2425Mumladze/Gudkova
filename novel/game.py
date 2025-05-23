import turtle as titi

from nvltho.novel import MainCharacter

titi.tracer(10)
wi = titi.Turtle()
wi.speed(0)
wi.hideturtle()
taxi = titi.Turtle()
taxi.speed(0)
taxi.hideturtle()
def square(x, y, line: bool, color='#f4cfcf'):
    wi.hideturtle()
    wi.up()
    wi.pencolor('black')
    wi.pensize(3)
    wi.fillcolor(color)
    wi.begin_fill()
    wi.goto(-x, y)
    wi.down()
    wi.goto(-x, -y)
    wi.goto(x, -y)
    wi.goto(x, y)
    wi.goto(-x, y)
    wi.end_fill()
    wi.up()
    if line:
        wi.hideturtle()
        wi.goto(0, y)
        wi.down()
        wi.goto(0, -y)
        wi.up()
def writef(text, x, y, l):
    taxi.hideturtle()
    taxi.up()
    taxi.goto(x, y)
    taxi.write(text, align="left", font=('Novel Sans Cy XCnd Medium', l, 'normal'))
titi.hideturtle()
#Вывод инвентаря\характеристик
def Char(char,inventory,cmd=False):
    def widget(colour='white'):
        wi.hideturtle()
        wi.up()
        wi.pencolor('#000000')
        wi.pensize(3)
        wi.fillcolor(colour)
        wi.begin_fill()
        wi.goto(-598, -250)
        wi.down()
        wi.goto(-598, -305)
        wi.goto(583, -305)
        wi.goto(583, -250)
        wi.goto(-598, -250)
        wi.end_fill()
        wi.up()
    square(583, 364, False, '#f4cfcf')
    square(505, 255, True, 'white')
    writef('Характеристики', -180, 300, 40)
    writef('Инвентарь', 135, 205, 35)

    def fill(char, x, y, hm=80):
        for i in char:
            writef(i, x, y, 30)
            y -= hm
    fill(char, -455, 180)
    fill(inventory, 30, 150, 40)
    if cmd:
        widget()
        writef('*Нажмите на кнопку на клавиатуре для выбора подарка. Нажмите на мышь, чтобы продолжить*',-500,-300,20)
def RemoveChar():
    wi.clear()
    taxi.clear()
#Вывод магазина
def Buy(balance, wn, cmd):
    def widget(colour='white'):
        wi.hideturtle()
        wi.up()
        wi.pencolor('#000000')
        wi.pensize(3)
        wi.fillcolor(colour)
        wi.begin_fill()
        wi.goto(-598, -250)
        wi.down()
        wi.goto(-598, -305)
        wi.goto(583, -305)
        wi.goto(583, -250)
        wi.goto(-598, -250)
        wi.end_fill()
        wi.up()
    square(583, 364, False, '#f4cfcf')
    square(505, 255, False, 'white')
    writef('Магазин', -120, 300, 40)
    writef(f'Баланс: {balance}',320,-215,20)
    tri = titi.Turtle()
    tri.pensize(5)
    tri.up()
    tri.hideturtle()
    flower = titi.Turtle()
    flower.hideturtle()
    mediator = titi.Turtle()
    mediator.hideturtle()
    fb = titi.Turtle()
    fb.hideturtle()
    m = titi.Turtle()
    m.hideturtle()
    flower.up()
    flower.goto(-375,145)
    wn.addshape('sprites\\flower.gif')
    flower.shape('sprites\\flower.gif')
    flower.showturtle()
    writef("Цена: 30", -400, 0, 15)
    mediator.up()
    wn.addshape('sprites\\mediator.gif')
    mediator.shape('sprites\\mediator.gif')
    mediator.goto(-75,145)
    mediator.showturtle()
    writef("Цена: 30", -100, 0, 15)
    fb.up()
    wn.addshape('sprites\\fb.gif')
    fb.shape('sprites\\fb.gif')
    fb.goto(225, 145)
    fb.showturtle()
    writef("Цена: 30", 200, 0, 15)
    m.up()
    wn.addshape("sprites\\m&m's.gif")
    m.shape("sprites\\m&m's.gif")
    m.goto(-375, -135)
    m.showturtle()
    writef("Цена: 50", -400, -240, 15)
    tri.fillcolor('#447d7d')
    tri.begin_fill()
    tri.goto(-119,-70)
    tri.down()
    tri.fd(150)
    tri.rt(120)
    tri.fd(150)
    tri.rt(120)
    tri.fd(150)
    tri.end_fill()
    tri.up()
    writef('Выход',-83,-123,25)
    if cmd==1:
        widget()
        writef('*Нажмите на нужный предмет для покупки. Для выхода нажмите на треугольник.*',-500,-300,20)
    elif cmd==2:
        widget()
        writef('*Недостаточно средств.*',-500,-300,20)
    # elif cmd==3:
        # fb.hideturtle()
        # wn.remove(m)
        # wn.remove(mediator)
        # wn.remove(flower)
def clearBuy(wn):
    wn.resetscreen()
    for ti in wn.turtles():
        ti.hideturtle()
#Запись информации в файл
def recordInfo(cm,gg:MainCharacter,ar,cl,va):
    nameOfEnding='-'
    if gg.ending==1:
        nameOfEnding='Учёная'
    elif gg.ending==2:
        nameOfEnding="С пушистыми"
    elif gg.ending == 3:
        nameOfEnding = 'Боевая'
    elif gg.ending == 4:
        nameOfEnding = 'Пропавшая'
    cc='w'
    if cm==1:
        cc='w'
    elif cm==2:
        cc='a'
    if cm!=3:
        with open('info\\mc all info.txt',cc) as f:
            f.write(f'{gg.name}\n')
            f.write('Инвентарь персонажа:\n')
            for i in gg.inventory:
                f.write(f'\t{i}\n')
            f.write('Ивентарь персонажа:\n')
            char=[gg.strength,gg.dexterity,gg.intelegence,gg.balance]
            charn=['Сила',"Ловкость","Интелект","Баланс"]
            for i in range(4):
                f.write(f'\t{charn[i]}:{char[i]}\n')
            f.write('Отношения с персонажами:\n')
            rel=[ar.rep,cl.rep,va.rep]
            reln=['Араши',"Хлоя","Валерин"]
            for i in range(3):
                f.write(f'\t{reln[i]}:{rel[i]}\n')
            f.write(f'Концовка: {nameOfEnding}\n')
            f.close()
    else:
        with open('info\\mc all info.txt', 'w') as f:
            pass