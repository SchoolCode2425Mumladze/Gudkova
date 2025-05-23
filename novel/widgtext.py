import turtle

wi = turtle.Turtle()
wi.speed(0)
wi.hideturtle()
#Диалоговое окно
def widget(colour='white'):
    wi.hideturtle()
    wi.up()
    wi.pencolor('#000000')
    wi.pensize(3)
    wi.fillcolor(colour)
    wi.begin_fill()
    wi.goto(-598,-201)
    wi.down()
    wi.goto(-598,-405)
    wi.goto(583, -405)
    wi.goto(583,-201)
    wi.goto(-598, -201)
    wi.end_fill()
    wi.up()
taxi=turtle.Turtle()
taxi.speed(0)
taxi.hideturtle()
tax=turtle.Turtle()
tax.speed(0)
tax.hideturtle()
#Вывод текста
def write(text):
    taxi.hideturtle()
    taxi.up()
    taxi.goto(-555, -250)
    if len(text)>70:
        text1=text[:71]
        taxi.write(text1, font=('Novel Sans Cy XCnd Medium', 24, 'normal'), align='left')
        if len(text[71:])>70:
            text2=text[71:142]
            taxi.goto(-555, -295)
            taxi.write(text2, font=('Novel Sans Cy XCnd Medium', 24, 'normal'), align='left')
            taxi.goto(-555, -340)
            taxi.write(text[142:], font=('Novel Sans Cy XCnd Medium', 24, 'normal'), align='left')
        else:
            text2=text[71:]
            taxi.goto(-555, -295)
            taxi.write(text2, font=('Novel Sans Cy XCnd Medium', 24, 'normal'), align='left')
    else:
        taxi.write(text, font=('Novel Sans Cy XCnd Medium', 24, 'normal'), align='left')
    taxi.color('black')
def removeWidjet():
    wi.clear()
#Большой текст
def writeNewChapter(text):
    tax.hideturtle()
    tax.up()
    tax.goto(-151,113)
    tax.write(text, font=('Novel Sans Cy XCnd Medium', 36, 'bold'), align='left')
#Вывод текста для выборов
def ShowChoice(first,second):
    taxi.hideturtle()
    taxi.up()
    taxi.goto(-555,-250)
    taxi.write(first,font=('Novel Sans Cy XCnd Medium',24,'normal'),align='left')
    taxi.goto(-555,-340)
    taxi.write(second,font=('Novel Sans Cy XCnd Medium',24,'normal'),align='left')
def ShowChar3(d,s,i):
    taxi.hideturtle()
    taxi.up()
    taxi.goto(-555,-250)
    taxi.write(d,font=('Novel Sans Cy XCnd Medium',24,'normal'),align='left')
    taxi.goto(-555,-290)
    taxi.write(s, font=('Novel Sans Cy XCnd Medium', 24, 'normal'), align='left')
    taxi.goto(-555,-330)
    taxi.write(i, font=('Novel Sans Cy XCnd Medium', 24, 'normal'), align='left')
def cleanText():
    taxi.clear()
    tax.clear()

