import turtle

wi = turtle.Turtle()
wi.speed(0)
wi.hideturtle()
def widget(colour='white'):
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

def write(text):

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
def writeNewChapter(text):
    taxi.up()
    taxi.goto(-151,113)
    taxi.write(text, font=('Novel Sans Cy XCnd Medium', 36, 'bold'), align='left')
def ShowChoice(first,second):
    taxi.up()
    taxi.goto(-555,-250)
    taxi.write(first,font=('Novel Sans Cy XCnd Medium',24,'normal'),align='left')
    taxi.goto(-555,-340)
    taxi.write(second,font=('Novel Sans Cy XCnd Medium',24,'normal'),align='left')
def ShowChar3(d,s,i):
    taxi.up()
    taxi.goto(-555,-250)
    taxi.write(d,font=('Novel Sans Cy XCnd Medium',24,'normal'),align='left')
    taxi.goto(-555,-290)
    taxi.write(s, font=('Novel Sans Cy XCnd Medium', 24, 'normal'), align='left')
    taxi.goto(-555,-330)
    taxi.write(i, font=('Novel Sans Cy XCnd Medium', 24, 'normal'), align='left')
def cleanText():
    taxi.clear()

