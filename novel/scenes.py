import novel.game
from novel import *

from nvltho.novel import cleanText, write, zombie, widget, Arashic

cmd=Choise(0)
def scene1(click,wd,x,y,gg:MainCharacter,cmd=cmd):

    def block1(click, wd):
        clicked = click.click

        text1 = ["Снова звонит будильник. Значит, пора вставать и собираться в школу.",
                 'Скоро поднимется ко мне в комнату отец и начнет бурчать, что бы я поторопилась.',
                 'Я ненавижу утро, так еще и тест по английскому в школе. Может притворится больной и никуда не пойти?',
                 '... ', 'Уже 10 минут прошло, а отца все нет. Он заболел? Или сегодня выходной? Странно это...']
        wd.bgpic('bg\\morning1.gif')
        cleanText()
        if clicked < 5:
            cleanText()
            write(text1[clicked])
        else:
            cleanText()
            choice = ['1.Пойти вниз к отцу.', "2.Остаться в комнате."]
            ShowChoice(choice[0], choice[1])
            if whichChoice(x, y) == 1:
                cmd.command = 1
            elif whichChoice(x, y) == 2:
                gg.balance += 10
                cmd.command = 2
        click.click2=0
    def block2(click,text):
        clicked2 = click.click2-1
        if clicked2 < len(text):
            cleanText()
            write(text[clicked2])
        else:
            cmd.command=3
            click.noClick()
    def block3(click,wd):
        cleanText()
        wd.bgpic('bg\\morning2.gif')
        text=['Темно…','Зайдя в гостиную, я увидела отца.']
        clicked=click.click-1
        if clicked < len(text):
            cleanText()
            write(text[clicked])
        if clicked==len(text):
            daddy.createSpriteDad(wd)
            widget(daddy.wcolour)
            write('.......')
            cmd.command=4
            click.noClick()
    def block4(click,wd):
        clicked=click.click
        text1=[f'Собирайся, {gg.name}. Мы уезжаем за город.','Папа, что происходит?','По новостям передают о распространени неизвестного вируса.' ,'Нужно скорее уезжать.Сосед сказал о базе, которую собираются создать за городом, поэтому быстрее бери самое важное и уходим.','...','Мне стало страшно, кое-как я вернулась в свою комнату и прихватила несколько вещей.']
        if clicked==1:
            cleanText()
            write(text1[0])
        elif clicked==2:
            widget(gg.colour)
            write(text1[1])
        elif clicked==3:
            widget(daddy.wcolour)
            write(text1[2])
        elif clicked==4:
            cleanText()
            write(text1[3])
        elif clicked==5:
            widget()
            write(text1[4])
        elif clicked==6:
            daddy.hideDad()
            cleanText()
            write(text1[5])
        elif clicked>6:
            cmd.command=5
            click.noClick()
    def block5(click,wd):
        text2=['Дорога.','Лес.','Новая жизнь.','Все это впереди и еще предстоит увидеть.']
        clicked=click.click
        cleanText()
        if clicked==1:
            wd.bgpic('nopic')
            wd.bgcolor('black')
            write('Так мы и уехали из дома…')
        elif clicked==2:
            cleanText()
            write('. . .')
        elif clicked==3:
            cleanText()
            wd.bgpic('bg\\destroitcity.gif')
            write('Город неузнаваем. Походу мир и впрямь сходит с ума.')
        elif 3<clicked<7:
            cleanText()
            write('. . .')
        elif clicked<len(text2)+7:
            wd.bgpic('bg\\road1.gif')
            cleanText()
            write(text2[clicked-7])
        elif clicked==11:
            widget(gg.colour)
            write('Мы справимся, мы обязательно справимся…')
            click.scenes+=1
            cmd.command=0
            click.noClick()

    if cmd.command==0:
        block1(click,wd)
    elif cmd.command==1:
        text=['Я пошла к отцу, взяв с собой лишь телефон.',
                'Вдруг, что-то взорвалось, да так, что затрясло всё здание.',
                'Что происходит?', '...',
                'Резко снизу послышался папин крик, и я побежала к нему с телефоном в руках.']
        block2(click,text)
    elif cmd.command==2:
        text=['Я решила не надумывать и пошла собираться в школу. ',
                'Уже собрав рюкзак я услышала взрыв, который сотряс всё здание, а после и крик отца.',
                'Взяв рюкзак с телефоном, я побежала вниз к нему.']
        block2(click,text)
    elif cmd.command==3:
        block3(click,wd)
    elif cmd.command==4:
        block4(click,wd)
    elif cmd.command==5:
        block5(click,wd)
def scene2(click,wd,x,y,gg:MainCharacter,cmd=cmd):
    def block1(click,wd):
        nameofchap='Глава первая: \nНовое начало'
        text=['Мы с отцом не можем найти себе места в мире апокалипсиса.' ,'К сожалению, все те базы, что мы успели объехать за месяц после начала хаоса, постоянно были либо разрушены нечестью, либо переполнены.' ,'Новая база встречает нас.' ,'У меня уже пропали надежды на спокойное существование, впрочем, даже если эта база и станет для нас новым домом, мы все равно больше не сможем жить как прежде.','Отец как всегда где-то пропадает, а я сижу, жду его на морозе здесь. Может пойти прогуляться?']
        clicked = click.click
        if clicked==1:
            wd.bgpic('nopic')
            wd.bgcolor('white')
            cleanText()
            removeWidjet()
            writeNewChapter(nameofchap)

        elif clicked>1 and clicked<=len(text)+1:
            cleanText()
            wd.bgpic('bg//camp.gif')
            widget()
            write(text[clicked-2])
        else:
            cleanText()
            choice = ['1.Пройтись по базе.', "2. Сидеть дальше."]
            ShowChoice(choice[0], choice[1])
            click.click2 = 0
            if whichChoice(x, y) == 1:
                gg.getNewItem('Красный мяч')
                cmd.command = 1
            elif whichChoice(x, y) == 2:
                gg.getNewItem('Вышивка')
                cmd.command = 2
    def block2(click,wd,text):
        clicked=click.click2-1
        if clicked<len(text):
            cleanText()
            write(text[clicked])
        else:
            cmd.command=3
            click.noClick()
    def block3(click,wd,gg):
        clicked=click.click-1
        text=['Вдруг начали шуршать кусты сзади меня. ', 'Обернувшись, я увидела…','Кота!']
        text2 = ['Дама, одетая явно не по сезону, бежала за котёнком.', 'Стоило ей закричать, как черныш скрылся.']
        if clicked<len(text):
            cleanText()
            write(text[clicked])
        else:
            if clicked==3:
                kitten.createSpriteCat(wd)
                widget(kitten.wcolor)
                write('...')
            elif clicked==4:
                cleanText()
                write('*мурчит*')
            elif clicked==5:
                widget(gg.colour)
                write('Ути какой малыш! Кс-кс-кс-кс-кс-кс-кс-кс, иди сюда!')
            elif clicked==6:
                kitten.hideCat()
                widget()
                write('За котёнком выбежала девушка.')
            elif clicked==7:
                Cloec.createSpriteCloe(wd)
                widget(Cloec.wcolour)
                write('Попался, жук белоусый!')
            elif clicked==8:
                Cloec.hideCloe()
                widget()
                write(text2[0])
            elif clicked==9:
                cleanText()
                write(text2[1])
            elif clicked==10:
                widget(Cloec.wcolour)
                Cloec.showCloe()
                write('Девушка, помоги мне поймать этого негодника, прошу!')
            else:
                cleanText()
                Cloec.hideCloe()
                widget()
                choice = ['1.Помочь.', "2. Уйти."]
                ShowChoice(choice[0], choice[1])
                click.click2 = 0
                if whichChoice(x, y) == 1:
                    gg.dexterity += 1
                    cmd.command = 4
                elif whichChoice(x, y) == 2:
                    cmd.command = 5
    def block4(click,text):
        clicked=click.click2-1
        if clicked==0:
            widget(gg.colour)
            write(text[0])
        elif clicked==1:
            widget()
            write(text[1])
        elif clicked==2:
            Cloec.showCloe()
            widget(Cloec.wcolour)
            write(text[clicked])
        elif clicked==3:
            cleanText()
            write(text[clicked])
        elif clicked==4:
            widget(gg.colour)
            write(text[clicked])
        elif clicked==5:
            widget(Cloec.wcolour)
            write(text[clicked])
        elif clicked>5:
            Cloec.hideCloe()
            widget()
            write(text[6])
            cmd.command=6
            click.noClick()
    def block5(click,text):
        clicked = click.click2 - 1
        if clicked==0:
            cleanText()
            write(text[clicked])
        elif clicked==1:
            Cloec.showCloe()
            widget(Cloec.wcolour)
            write(text[clicked])
        elif clicked>1:
            Cloec.hideCloe()
            widget()
            write(text[2])
            cmd.command = 6
            click.noClick()
    def block6(click,wn):
        clicked=click.click-1
        text1=['После этой странной встречи отец всё-таки вернулся ко мне.','Он рассказал о том, что мы можем остаться здесь, но только при условии, если мы будем работать.',
               'Отец не хотел подвергать меня опасности, и я его понимаю. Еще месяц назад я была ученицей выпускного класса, а сейчас буду выходить на смертельные вылазки ради припасов.',
               'Но я уже достаточно взрослая чтобы заботится о себе самой. Не так ли?']

        if clicked<len(text1):
            cleanText()
            write(text1[clicked])
        else:
            wd.bgpic('bg\\campfire.gif')
            if clicked==4:
                cleanText()
                write('Вечерело. Разожгли костер. Вокруг него уже собирались люди, лишь несколько человек предпочли оставаться в тени мёрзлых теней.')
            elif clicked==5:
                cleanText()
                write('Один из стоящих в темноте спустил очки на кончик носа и взглянул на меня. ')
            elif clicked==6:
                Arashic.createSpriteArashi(wn)
                widget(Arashic.wcolour)
                write('...')
            elif clicked>6:
                widget()
                choice = ['1.Уйти.', "2.Подойти"]
                ShowChoice(choice[0], choice[1])
                click.click2 = 0
                if whichChoice(x, y) == 1:
                    Arashic.hideArashi()
                    cmd.command = 7
                elif whichChoice(x, y) == 2:
                    cmd.command = 8
    def block7(click,gg,helped:bool):
        clicked = click.click2 - 1
        text1=['Выглядел незнакомец необычно, но сейчас желания с кем-либо знакомится нет, поэтому лучше мне уйти.','Стоило мне сделать шаг от костра, как я почувствовала чьё-то присутствие сзади.',
              'Привет, незнакомка. Ты из новоприбывших?',f'Угу. Меня зовут {gg.name}.', 'А те…','Меня зовут Араши. Приятно познакомится, ненезнакомка.',
              'Ага, очень.','Прости, мне пора.']
        if clicked==0 or clicked==1:
            widget()
            cleanText()
            write(text1[clicked])
        elif clicked==2:
            Arashic.showArashi()
            widget(Arashic.wcolour)
            write(text1[clicked])
        elif clicked==3 or clicked==4:
            widget(gg.colour)
            write(text1[clicked])
        elif clicked==5:
            widget(Arashic.wcolour)
            write(text1[clicked])
        elif 6<=clicked<=7:
            widget(gg.colour)
            write(text1[clicked])
        elif helped and clicked>7:
            Arashic.mcName='Занятая'
            text2 = ['У тебя, занятая, здесь успела появится репутация добродушной леди.', 'Походу краса твоей души мне не светит.',
                'Репутация? О чем ты?', 'Хлоя, местная помешанная на животных, говорила о твоей помощи ей.', ]
            if 8<=clicked<=9:
                widget(Arashic.wcolour)
                write(text2[clicked-8])
            elif clicked==10:
                widget(gg.colour)
                write(text2[clicked-8])
            elif clicked==11:
                widget(Arashic.wcolour)
                write(text2[clicked-8])
                click.noClick()
                cmd.command = 9
        elif clicked>7 and not helped:
            Arashic.mcName='Злюка'
            text3 = ['Знаешь, злюка, тебе бы лучше быть подобрее. В мире, полного хаоса иметь плохую репутацию невыгодно.',
                'Репутацию? Я только приехала сюда, какая может быть у меня репутация.',
                'Уж не знаю, как меньше чем за сутки ты смогла обидеть нашу помешанную на животных Хлою.',
                'Хлою? Ты про дамочку с котёнком?',
                'Да. Обычно она добра со всеми, но твое безразличие ее ранило, так как из-за него ее пушистик совсем замёрз и болеет.',
                'Чёрт, надо было помочь ей тогда…']
            if 8<=clicked<=12 and clicked%2==0:
                widget(Arashic.wcolour)
                write(text3[clicked-8])
            elif 9<=clicked<=11 and clicked%2!=0:
                widget(gg.colour)
                write(text3[clicked-8])
            elif clicked==13:
                widget()
                write(text3[-1])
                click.noClick()
                cmd.command = 9
    def block8(click,gg,helped:bool):
        clicked=click.click2-1
        text1=['Стоит познакомится с людьми здесь. Всё-таки мне тут ещё жить...',f'Привет, меня зовут {gg.name}. Я прибыла сюда недавно.','Новенькая, привет! Меня зовут Араши.']
        if clicked==0:
            widget()
            write(text1[0])
        elif clicked==1:
            widget(gg.colour)
            write(text1[clicked])
        elif clicked==2:
            widget(Arashic.wcolour)
            write(text1[clicked])
        elif clicked>2 and helped:
            Arashic.mcName='Спасительница'
            text2=['Признаюсь, шума ты наделала. Можно я буду тебя называть героем?','Мм? О чём ты?','Местная кошатница жужжала мне на ухо весь день про новенькую, которая помогла ей с поимкой пушистого демона.',
                   'А, так то пустики! Но прошу, не зови меня героем. Это неловко, лучше просто зови по имени.','Не обещаю, ой, не обещаю, спасительница.','Хм-м, он, конечно, добр ко мне, но в каждом его слове чувствуется насмешка. Странный он.']
            if 3<=clicked<=7 and clicked%2!=0:
                widget(Arashic.wcolour)
                write(text2[clicked-3])
            elif 4<=clicked<=6 and clicked%2==0:
                widget(gg.colour)
                write(text2[clicked-3])
            elif clicked==8:
                widget()
                write(text2[clicked-3])
                click.noClick()
                cmd.command=9

        elif clicked > 2 and not helped:
            Arashic.mcName ="Добрючка"
            text3=['Ожидал, что ты будешь злючнее. Походу словам Хлои лучше не верить.','Мм? О чём ты?','Местная кошатница ныла мне весь день про новенькую, которая проигнорировала просьбы о помощи невинной, бедной Хлоички.',
                   'Это, пожалуй, не далеко от правды, но…','Не оправдывайся. Я всё понимаю!','Араши добр ко мне, хотя я и поступила не очень хорошо. Говорит это о его добродушии или же о темноте души?']
            if 3 <= clicked <= 7 and clicked % 2 != 0:
                widget(Arashic.wcolour)
                write(text3[clicked - 3])
            elif 4 <= clicked <= 6 and clicked % 2 == 0:
                widget(gg.colour)
                write(text3[clicked - 3])
            elif clicked == 8:
                widget()
                write(text3[clicked - 3])
                click.noClick()
                cmd.command = 9
    def block9(click,gg):
        clicked=click.click
        text1=[f'Забудем. Ты кем собираешься быть, {Arashic.mcName}: учёной, разведчиком или же собирателем ресурсов?','Пока не знаю, до апокалипсиса я хотела быть музыкантом. Думаю, сейчас это не актуально.',
               'Что ты же ты так. Творческая душа твоя прекрасно себя проявит в собирании ягод и в вытирании пыли с корешков библиотечных книг! Не жизнь, а мечта!','Что же ты делаешь для базы? Вижу, ты не менее интересная личность.','Моя душа ищет свободы. Это банально и обыденно, но я не хочу быть запертым в этом чёртовом лагере с иллюзией выбора, поэтому я предпочту рисковать жизнью, только лишь увидеть горизонт и подобие свободы.',
               'Свободы не будет, пока по земле ходят зомби или подобные им люди.','Подобные люди?',
               'Ага. Ходит слух, что зомби становятся убийцы. То есть, все зомби в каком-то смысле были монстрами и до апокалипсиса.',f'Даже если человек защищал себя, или сделал это случайно, он становится зомби? Что я могу сказать, {Arashic.mcName}? Надежд на спасение точно нет!',
               "Предполагаю, даже зомби убивать нельзя, так как они в каком-то смысле тоже люди?",'К сожалению, это так…','Мрачная атмосфера. Опять.','И опять её прервала она…','Привет, Араши. Привет, новенькая.']
        if 0<=clicked<=8 and clicked%2==0 or clicked==9:
            widget(Arashic.wcolour)
            write(text1[clicked])
        elif 1<=clicked<=7 and clicked%2!=0 or clicked==10:
            widget(gg.colour)
            write(text1[clicked])
        elif 11<=clicked<=12:
            Arashic.hideArashi()
            widget()
            write(text1[clicked])
        elif clicked==13:
            Cloec.showCloe()
            widget(Cloec.wcolour)
            write(text1[clicked])
        if Cloec.rep<0 and 14<=clicked<=15:
            if clicked==14:
                widget(gg.colour)
                write(f'Я {gg.name}. И насчет твоего кота, прости меня.')
            elif clicked==15:
                widget(Cloec.wcolour)
                write('Ничего такого! Опять эта атмосфера…')
        elif clicked==16 and Cloec.rep<0 or Cloec.rep>0 and clicked==14:
            cleanText()
            write('Давайте пойдём хоть погуляем! Чего вы тут как два столба стоите!')
        elif clicked == 17 and Cloec.rep < 0 or Cloec.rep > 0 and clicked == 15:
            Cloec.hideCloe()
            Arashic.showArashi()
            widget(Arashic.wcolour)
            write('Пас')
        elif clicked==18 and Cloec.rep<0 or Cloec.rep>0 and clicked==16:
            Arashic.hideArashi()
            widget()
            write('Теперь не такой многословный Араши ушёл…')
            click.noClick()
            cmd.command=10
    def block10(click,wd,gg):
        clicked = click.click-1
        text1=[f'А ты, {gg.name}? Xочешь куда-нибудь пойти? Я могу показать тебе тут всё!','Прости, Хлоя. Пожалуй мне лучше пойти уже спать...','Тогда я тебя провожу.','Так мы и пошли к базе. Хлоя болтала о людях здесь, о своём коте. Потом ещё о своём коте. Теперь я понимаю Араши...','Ой, заболталась я. Завтра утром приходи в общую столовую. Там я с тобой обсужу вечеринку.',
               'Вечеринку? В такое время?','А почему нет? Да и не так уж всё помпезно будет. Просто посидим у костра, поболтаем, попоём и всё такое. Нужно же как-то жить дальше...','Может ты и права.']

        if 0<=clicked<=6 and clicked%2==0:
            Cloec.showCloe()
            widget(Cloec.wcolour)
            write(text1[clicked])
        elif 1<=clicked<=7 and clicked%2!=0 and clicked!=3:
            widget(gg.colour)
            write(text1[clicked])
        elif clicked==3:
            widget()
            write(text1[3])
        elif clicked==8:
            wd.bgpic('bg\\camp.gif')
            widget()
            Cloec.hideCloe()
            write('За беседой незаметно пробежало время. Так, я уже стояла возле базы. Хлоя быстро попрощалась со мной и убежала.')
        elif clicked>=9 and clicked<=12:
            Cloec.hideCloe()
            wd.bgpic('bg\\room.gif')
            text2=['Переодевшись в лёгкую одежду, я улеглась на кровать и начала думать над словами Араши...','Пол жизни я потратила на размышление о будущем, и кое-как я решилась быть музыкантом. Теперь у меня есть три пути, и все они далеки от меня.','Если так подумать, я не имею никаких навыков для апокалипсиса.','Для учёной нужно быть умной, для разведчика-сильной, для собирательства-ловкой.']
            cleanText()
            write(text2[clicked-9])
        else:
            cleanText()
            choice = ['1.Показать статы.', "2. Не показывать статы."]
            ShowChoice(choice[0], choice[1])
            if whichChoice(x, y) == 1:
                click.click2=0
                cmd.command = 11
            elif whichChoice(x, y) == 2:
                click.click = 0
                cmd.command = 12
    def block11(click,gg):
        clicked = click.click2-1
        if clicked==0:
            removeWidjet()
            cleanText()
            readChar()
            char=readChar(True)
            novel.game.Char(char,gg.inventory)
        elif clicked==2:
            click.click = 0
            novel.game.RemoveChar()
            cmd.command=12
    def block12(click,wd,gg):
        clicked=click.click-1
        widget()
        text1=['Ладно, буду думать об этом позже. Сейчас время для сна.','...','Настало утро.',"Как говорила Хлоя, я пошла в столовую.","Хлоя махала мне рукой за одним из столиков. Рядом с ней сидел Араши.",
               "Когда я набрала поднос еды рядом со мной проходила неприметная девушка. Она пыталась пройти как можно скорее, и случайно зацепила меня.", "Наши подносы полетели вниз, но каким-то образом только её всю одежду замарала еда."]
        if clicked<=6:
            if clicked==3:
                wd.bgpic('bg\\cafitaria.gif')
            cleanText()
            write(text1[clicked])
        elif clicked>6:
            cleanText()
            choice = ['1.Помочь девушке встать.', "2.Убрать беспорядок."]
            ShowChoice(choice[0], choice[1])
            if whichChoice(x, y) == 1:
                gg.intelegence+=1
                gg.getNewItem('Книга')
                Cloec.rep+=5
                Arashic.rep-=5
                click.click2 = 0
                cmd.command = 13
            elif whichChoice(x, y) == 2:
                gg.getNewItem('Сладости')
                gg.dexterity+=2
                Arashic.rep+=5
                Cloec.rep-=5
                click.click2 = 0
                cmd.command = 14
    def block13(click,gg,text):
        clicked = click.click2 - 1
        if clicked<len(text):
            cleanText()
            write(text[clicked])
        else:
            click.noClick()
            cmd.command=15
    def block14(click,gg,wd):
        clicked=click.click-1
        text1=['После этого случая, я пошла гулять по базе. От помощи Хлои я сразу отказалась.','Глаза нашли библиотеку с пожелтевшей вывеской.','Зайдя внутрь, я учуяла запах дерева и пыли. Ели как сдержав чих, я заметила девушку и мальчика, читавших книгу.',
               'Девушка, сидя на полу, держала в руках огромный пыльный томик.','На её плече лежала голова мальчика.', 'Они похожи. Может они-брат и сестра?','Проигнорировав их, я пошла смотреть на томики…']
        if clicked<2:
            cleanText()
            write(text1[clicked])
        elif clicked==2:
            wd.bgpic('bg\\library.gif')
            cleanText()
            write(text1[2])
        elif clicked==3:
            valerinC.createSpriteValerin(wd)
            widget()
            write(text1[clicked])
        elif clicked==4:
            valerinC.hideValerin()
            vernon.createSpriteVernon(wd)
            widget()
            write(text1[4])
        elif 5<=clicked<=6:
            vernon.hideVernon()
            cleanText()
            write(text1[clicked])
        else:
            cleanText()
            choice = ['1.Почитать книги.', "2.Помочь библиотекарше."]
            ShowChoice(choice[0], choice[1])
            if whichChoice(x, y) == 1:
                gg.intelegence += 1
                click.click2 = 0
                cmd.command = 16
            elif whichChoice(x, y) == 2:
                gg.strength+=1
                gg.balance+=10
                click.click2 = 0
                cmd.command = 17
    def block15(click,text):
        clicked=click.click2-1
        if clicked<len(text):
            cleanText()
            write(text[clicked])
        else:
            click.noClick()
            cmd.command=18
    def block16(click,gg):
        clicked=click.click-1
        text1=['Времени прошло много. Я уже хотела выходить, но мне на глаза бросилась девушка с книгой. Та самая, что я встретила ещё несколько часов назад. Её поза не изменилась, она так-же продолжала читать.','Может подойти познакомиться?','Не думая более, я подошла к ней.',f'Привет! Я {gg.name}, хотела познакомиться с тобой!',
    'Угу. Меня зовут Валерин. Мальчишка внизу-мой брат. Его зовут Вернон.','М-м-м...','Извини, я немного в размышлениях сейчас. Не могла бы ты уйти?','Я только подошла, а меня уже шлют…']
        if clicked<8:
            if clicked<3:
                widget()
                write(text1[clicked])
            elif clicked==3:
                valerinC.showValerin()
                widget(gg.colour)
                write(text1[3])
            elif 4<=clicked<=6:
                widget(valerinC.wcolour)
                write(text1[clicked])
            elif clicked==7:
                widget()
                write(text1[7])
        else:
            cleanText()
            choice = ['1.Уйти.', "2.Остаться."]
            ShowChoice(choice[0], choice[1])
            if whichChoice(x, y) == 1:
                valerinC.rep+=10
                click.click2 = 0
                cmd.command = 19
            elif whichChoice(x, y) == 2:
                valerinC.rep-=10
                click.click2 = 0
                cmd.command = 20
    def block17(click,text):
        clicked=click.click2-1
        if len(text)==3:
            if clicked==0:
                widget(gg.colour)
                write(text[0])
            elif 0<clicked<3:
                valerinC.hideValerin()
                widget()
                write(text[clicked])
            else:
                cleanText()
                click.scenes += 1
                cmd.command = 0
                click.noClick()
        else:
            if clicked==2:
                widget(valerinC.wcolour)
                write(text[clicked])
            elif clicked!=2 and clicked<4:
                widget(gg.colour)
                write(text[clicked])
            elif clicked==4:
                widget()
                valerinC.hideValerin()
                write(text[clicked])
            elif clicked==5:
                cleanText()
                write(text[clicked])
            elif clicked==6:
                cleanText()
                click.scenes += 1
                cmd.command = 0
                click.noClick()

    if cmd.command==0:
        block1(click,wd)
    elif cmd.command==1:
        text=['Снежок приукрасил гнетущую серость улиц. Впрочем, это ненадолго. Скоро он лишь станет слякотью, и будет омрачать и так унылые улочки.','Люди вокруг шумели, радуясь. Их настроение я разделить не могу. Все гнетет, мысли лезут в голову. Несмотря на апокалипсис, на небе беззаботно сияет солнце. Его лучи-единственное, что хоть как-то заставляет двигаться дальше…'
            ,'Вдруг, моя нога наступила на что-то круглое. ','Это был красный мячик.','Я подняла его, чтобы рассмотреть поближе. Он неожиданно поднял мне настроение, и я решила взять его с собой.','*Красный мяч добавлен в инвентарь* ']
        block2(click,wd,text)
    elif cmd.command==2:
        text=['Было холодно. Снежинки падали на красный нос, уже немели руки.','Хотелось вернуться домой, скрыться от грозной бури под одеялом в тёпленькой кроватке.','Ветер обдувал щеки, отчего они нещадно болели.','Внезапно, к моим ногам прилетела нашивка.','Кое-как подняв ее, я начала рассматривать дизайн черного кругляшка. На нем был логотип группы Iron Maiden.'
              ,'*Вышивка добавлена в инвентарь*']
        block2(click,wd,text)
    elif cmd.command==3:
        block3(click,wd,gg)
    elif cmd.command==4:
        text=['Хорошо.','Общими усилиями спустя минут пять бегун был найден.','Спасибо! Э-э-э-э…','Как тебя зовут, моя спасительница?',f'{gg.name}.',f'А меня-Хлоя! Еще раз спасибо,{gg.name}. Мне нужно бежать, а то я себе всё застужу скоро. Брр…','Я не успела и словo вставить, как эта странная парочка испарилась.']
        block4(click,text)
        Cloec.rep=10
    elif cmd.command==5:
        text =['Я быстро убежала от этой странной дамы.','Ах? Чёрт, не убегай!','Девушка побежала за котёнком и в скором времени пропала из моего поля зрения.']
        block5(click,text)
        Cloec.rep=-10
    elif cmd.command==6:
        block6(click,wd)
    elif cmd.command==7:
        Arashic.rep=10
        helped = False
        if Cloec.rep > 0:
            helped = True
        block7(click,gg,helped)
    elif cmd.command==8:
        Arashic.rep=5
        helped=False
        if Cloec.rep>0:
            helped=True
        block8(click,gg,helped)
    elif cmd.command==9:
        block9(click,gg)
    elif cmd.command==10:
        block10(click,wd,gg)
    elif cmd.command==11:
        block11(click,gg)
    elif cmd.command==12:
        block12(click,wd,gg)
    elif cmd.command==13:
        text=['Одежда девушки была вся испачкана.', 'Как только она встала на ноги, я повела её в туалет, дабы хоть как-то помочь ей отмыть пятна с ткани. Позже девушка побежала в свою комнатку переодеться.',' Я пошла за ней.' ,'Вышла же она с интересным вознаграждением в виде книги.',
        '*Книга добавлена в инвентарь.*','Робко идя позади меня, девушка рассказывала об открытиях, связанных с апокалипсисом. Я с интересом слушала её.']
        block13(click,gg,text)
    elif cmd.command==14:
        text=['Я быстро отнесла весь мусор с подносами на кухню в столовой.',' Отмыв все тарелки, я получила конфетку от поварихи.',"*Сладости были добавлены в инвентарь.*"]
        block13(click,gg,text)
    elif cmd.command==15:
        block14(click,gg,wd)
    elif cmd.command==16:
        text=['Я нашла простенький томик и начала читать его.',"*+1 интеллект.*"]
        block15(click,text)
    elif cmd.command==17:
        text=['Я помогла милой женщине, перенеся тяжёлые книги на полки.',"*+1 сила.*",'*+10 баланс.*']
        block15(click,text)
    elif cmd.command==18:
        block16(click,gg)
    elif cmd.command==19:
        text=['Ладно. Ещё свидимся!','Так я ушла от этой странной дамы. Если так подумать, все тут такие странные. Один с синдромом восьмиклассника, другая помешанная на котах, третья вредная.','Тяжело…']
        block17(click, text)
    elif cmd.command==20:
        text=['Я тебя чем-то обидела?','Я просто хотела познакомится.','Не обидела, просто я вредная и очень люблю находится в тишине без посторонних.','Ладно, прощай.','Так я ушла от этой странной дамы. Если так подумать, все тут такие странные. Один с синдромом восьмиклассника, другая помешанная на котах, третья вредная.','Тяжело…']
        block17(click,text)
def scene3(click,wd,x,y,gg:MainCharacter,cmd=cmd):
    def block1(click, gg ):
        clicked = click.click - 1
        if clicked == 0:
            wd.bgpic('nopic')
            wd.bgcolor('white')
            cleanText()
            removeWidjet()
            writeNewChapter('Несколько часов спустя')
        else:
            clicked -= 1
            text1 = ['Я пришла к костру. Тут собрались все: дети, подростки, взрослые и старики.',
                     ' Дети прыгали у костра, их родители ворчали на них.',
                     'Некоторые взрослые стояли возле еды и с набитыми ртами, чуть ли не плюясь, спорили о разном.',
                     'Некоторая часть людей сидела у костра и играла на инструментах, танцевала, пела.',
                     'Поискав знакомые лица, я заметила Валерин с её братом под кроном дерева.',
                     'Валерин играла на флейте, Вернон же мычал в унисон.',
                     'Отец вместе с взрослыми уже распивал очередную кружечку алкоголя.',
                     'Хлоя сидела возле костра со своей кошкой-Луной, качаясь, словно на её руках не кот, а ребёнок.',
                     'Араши же сидел рядом, брынькал на старой гитаре.']
            if clicked == 0:
                cleanText()
                wd.bgpic('bg\\party.gif')
                widget()
                write(text1[clicked])
            elif clicked < len(text1):
                cleanText()
                write(text1[clicked])
            else:
                cleanText()
                choice = ['1.Подойти к Валерин.', "2.Подойти к Хлое с Араши."]
                ShowChoice(choice[0], choice[1])
                if whichChoice(x, y) == 1:
                    valerinC.rep += 10
                    click.click2 = 0
                    cmd.command = 1
                elif whichChoice(x, y) == 2:
                    click.click2=0
                    cmd.command=3

    def block2(click,wn):
        clicked = click.click2 - 1
        text1 = ['Привет. Можно я устроюсь рядом с вами?', 'Не…', 'Конечно можно.',
                 'Я не хотела прерывать идилию, поэтому лишь тихо сидела и слушала импровизацию ребят.',
                 'Как только Валериан закончила, она с блеском в глазах посмотрела на меня.',
                 'Мне захотелось подарить ей что-то.']
        if clicked == 0:
            valerinC.showValerin()
            widget(gg.colour)
            write(text1[clicked])
        elif clicked == 1:
            widget(valerinC.wcolour)
            write(text1[1])
        elif clicked == 2:
            valerinC.hideValerin()
            vernon.showVernon()
            widget(vernon.wcolour)
            write(text1[2])
        elif clicked > 2 and clicked < len(text1):
            vernon.hideVernon()
            widget()
            write(text1[clicked])
        else:
            cleanText()
            choice = ['1.Подарить.', "2.Ничего не дарить."]
            ShowChoice(choice[0], choice[1])
            if whichChoice(x, y) == 1:
                click.button = None
                cmd.command = 2
                click.click=0
            elif whichChoice(x, y) == 2:
                click.noClick()
                cmd.command = 8

    def block3(click, gg):
        clicked = click.click-1
        but = click.button
        removeWidjet()
        cleanText()
        readChar()
        char = readChar(True)
        readInventory()
        invent = readInventory(True)
        if clicked == 0:
            novel.game.Char(char, invent, True)
        if but != None:
            novel.game.RemoveChar()
            if int(but) <= len(gg.inventory):
                item = gg.inventory[int(but) - 1]
                if item in valerinC.favorites:
                    if clicked == 1:
                        valerinC.showValerin()
                        widget(valerinC.wcolour)
                        write('Спасибо. Мне нравится.')
                    elif clicked == 2:
                        widget()
                        write('Я увидела, что улыбка её и впрямь искреняя.')
                    else:
                        valerinC.hideValerin()
                        valerinC.rep += 20
                        gg.inventory.pop(int(but) - 1)
                        readChar()
                        click.noClick()
                        cmd.command = 8
                else:
                    if clicked == 1:
                        valerinC.showValerin()
                        widget(valerinC.wcolour)
                        write('Боюсь, подобное не для меня…')
                    else:
                        valerinC.hideValerin()
                        valerinC.rep -= 20
                        readChar()
                        gg.inventory.pop(int(but)-1)
                        click.noClick()
                        cmd.command = 8
            else:
                if clicked == 1:
                    widget()
                    write('Я решила ничего не дарить.')
                elif clicked==2:
                    cleanText()
                    click.noClick()
                    cmd.command=8
    def block4(click):
        cleanText()
        choice = ['1.Подойти к Араши.', "2.Подойти к Хлое."]
        ShowChoice(choice[0], choice[1])
        if whichChoice(x, y) == 1:
            cmd.command = 4
            click.click = 0
        elif whichChoice(x, y) == 2:
            cmd.command=6
            click.click=0
    def block5(click,gg,wn):
        clicked=click.click-1
        text1=['Можно мне поиграть?','Да, конечно. Как я могу оставить нашу творческую душу без её крыльев.','Закатив глаза, я взяла гитару.','Когда я начала играть, вместо его обычной ухмылки, я увидела искреннее восхищение.','Захотелось ему что-то подарить.']
        cleanText()
        if clicked==0:
            Arashic.showArashi()
            widget(gg.colour)
            write(text1[clicked])
        elif clicked==1:
            widget(Arashic.wcolour)
            write(text1[1])
        elif 2<=clicked<=4:
            widget()
            write(text1[clicked])
        else:
            choice = ['1.Подарить.', "2.Ничего не дарить."]
            ShowChoice(choice[0], choice[1])
            if whichChoice(x, y) == 1:
                click.button = None
                cmd.command = 5
                click.click2 = 0
                Arashic.hideArashi()
            elif whichChoice(x, y) == 2:
                click.noClick()
                cmd.command=8
    def block6(click,gg):
        clicked = click.click2 - 1
        but = click.button
        removeWidjet()
        cleanText()
        readChar()
        char = readChar(True)
        readInventory()
        invent = readInventory(True)
        if clicked == 0:
            novel.game.Char(char, invent, True)
        if but != None:
            novel.game.RemoveChar()
            if int(but) <= len(gg.inventory):
                item = gg.inventory[int(but) - 1]
                if item in Arashic.favorites:
                    if clicked == 1:
                        Arashic.showArashi()
                        widget(Arashic.wcolour)
                        write(F'Ого, {Arashic.mcName}. Ты такая щедрая! Спасибочки.')
                    elif clicked == 2:
                        widget()
                        write('Его реакция пугала, но фальшивой не была. Это, наверно, хорошо?')
                    else:
                        Arashic.hideArashi()
                        Arashic.rep += 20
                        gg.inventory.pop(int(but) - 1)
                        readChar()
                        click.noClick()
                        cmd.command = 8
                else:
                    if clicked == 1:
                        Arashic.showArashi()
                        widget(Arashic.wcolour)
                        write('Ты считаешь меня мусором? Поэтому даришь соответствующее? Ты так внимательна! Спасибо!')
                    else:
                        Arashic.hideArashi()
                        Arashic.rep -= 20
                        readChar()
                        gg.inventory.pop(int(but) - 1)
                        click.noClick()
                        cmd.command = 8
            else:
                if clicked == 1:
                    widget()
                    write('Я решила ничего не дарить.')
                elif clicked==2:
                    cleanText()
                    click.noClick()
                    cmd.command=8
    def block7(click,gg,wd):
        clicked = click.click - 1
        text1 = ['Можно погладить Луну?', 'Конечно!',
                 '*мурчит*',
                 'Хлоя может и необычная, но явно добрая.',
                 'Мне захотелось подарить ей что-то.']
        cleanText()
        if clicked == 0:
            Cloec.showCloe()
            widget(gg.colour)
            write(text1[clicked])
        elif clicked == 1:
            widget(Cloec.wcolour)
            write(text1[1])
        elif clicked ==2:
            Cloec.hideCloe()
            kitten.showCat()
            widget(kitten.wcolor)
            write(text1[2])
        elif 3 <= clicked <= 4:
            kitten.hideCat()
            widget()
            write(text1[clicked])
        else:
            choice = ['1.Подарить.', "2.Ничего не дарить."]
            ShowChoice(choice[0], choice[1])
            if whichChoice(x, y) == 1:
                click.button = None
                cmd.command = 7
                click.click2 = 0
            elif whichChoice(x, y) == 2:
                click.noClick()
                cmd.command = 8
    def block8(click,gg):
        clicked = click.click2 - 1
        but = click.button
        removeWidjet()
        cleanText()
        readChar()
        char = readChar(True)
        readInventory()
        invent = readInventory(True)
        if clicked == 0:
            novel.game.Char(char, invent, True)
        if but != None:
            novel.game.RemoveChar()
            if int(but) <= len(gg.inventory):
                item = gg.inventory[int(but) - 1]
                if item in Cloec.favorites:
                    if clicked == 1:
                        Cloec.showCloe()
                        widget(Cloec.wcolour)
                        write('Это мне? Огромное спасибо!')
                    elif clicked == 2:
                        widget()
                        write('Она начала пританцововать полная счастья.')
                    else:
                        Cloec.hideCloe()
                        Cloec.rep += 20
                        gg.inventory.pop(int(but) - 1)
                        readChar()
                        click.noClick()
                        cmd.command = 8
                else:
                    if clicked == 1:
                        Cloec.showCloe()
                        widget(Cloec.wcolour)
                        write('Ох, я… Найду этому применение.')
                    else:
                        Cloec.hideCloe()
                        Cloec.rep -= 10
                        readChar()
                        gg.inventory.pop(int(but) - 1)
                        click.noClick()
                        cmd.command = 8
            else:
                if clicked == 1:
                    widget()
                    write('Я решила ничего не дарить.')
                elif clicked==2:
                    cleanText()
                    click.noClick()
                    cmd.command=8
    def block9(click,wd):
        clicked=click.click-1
        if clicked==0:
            cleanText()
            widget()
            write('Думаю, уже пора уйти домой. Завтра надо будет работать…')
        elif clicked==1:
            cleanText()
            wd.bgpic('nopic')
            wd.bgcolor('white')
            removeWidjet()
            writeNewChapter('Следущий день')
            click.scenes += 1
            cmd.command = 0
            click.noClick()
    if cmd.command==0:
        block1(click,gg)
    elif cmd.command==1:
        block2(click,wd)
    elif cmd.command==2:
        block3(click,gg)
    elif cmd.command==3:
        block4(click)
    elif cmd.command==4:
        block5(click, gg,wd)
    elif cmd.command==5:
        block6(click,gg)
    elif cmd.command==6:
        block7(click,gg,wd)
    elif cmd.command==7:
        block8(click,gg)
    elif cmd.command==8:
        block9(click,wd)
def scene4(click,wd,x,y,gg:MainCharacter,cmd=cmd):
    def workout(click,wd,cmdm):
        clicked=click.click2-1
        if clicked==0:
            wd.bgpic('bg\\gym.gif')
            widget()
            write('Занятия спортом укрепили моë тело.')
        elif clicked==1:
            cleanText()
            write('Во время упражнений я увидела Араши. Похоже, ему понравился мой боевой настрой.')
        elif clicked==2:
            cleanText()
            write('*+2 сила*')
        else:
            cleanText()
            click.click2=0
            click.noClick()
            Arashic.rep += 5
            gg.strength += 2
            cmd.command=cmdm
    def library(click,wd,cmdm):
        clicked=click.click2-1
        if clicked==0:
            wd.bgpic('bg\\library.gif')
            widget()
            write('Много новой информации... Мозги кипят!')
        elif clicked==1:
            cleanText()
            write('Вивьен смотрела на меня из своего угла. Походу ей любопытно за мной наблюдать.')
        elif clicked==2:
            cleanText()
            write('*+1 интеллект*')
        if 'Книга' in gg.inventory:
            if clicked==3:
                cleanText()
                write('У меня ещё осталась книга от той девы.')
            elif clicked>3:
                cleanText()
                choice = ['1.Прочесть и оставить в библиотеке.', "2.Оставить её себе."]
                ShowChoice(choice[0], choice[1])
                if whichChoice(x, y) == 1:
                    cleanText()
                    write('*+1 интеллект*')
                    gg.inventory.pop(gg.inventory.index('Книга'))
                    gg.intelegence += 1
                    gg.intelegence += 2
                    valerinC.rep += 5
                    click.noClick()
                    click.noClick()
                    cmd.command=cmdm
                elif whichChoice(x, y) == 2:
                    cleanText()
                    write('Пожалуй, лучше её оставить.')
                    gg.intelegence += 1
                    valerinC.rep += 5
                    click.noClick()
                    cmd.command = cmdm
        else:
            if clicked==3:
                cleanText()
                click.click2=0
                click.noClick()
                gg.intelegence += 1
                valerinC.rep += 5
                cmd.command=cmdm
    def walking(click,wd,cmdm):
        clicked=click.click2-1
        if clicked==0:
            wd.bgpic('bg\\street.gif')
            widget()
            write('Холод освежает. Я уже чувствую как телo привыкает к подoбным нагрузкам!')
        elif clicked==1:
            cleanText()
            write('Хлоя прогуливалась со своим котом. Заметив меня, она лучезарно улыбнулась.')
        elif clicked==2:
            cleanText()
            write('*+1 ловкость*')
        else:
            cleanText()
            click.click2=0
            click.noClick()
            gg.dexterity += 1
            Cloec.rep += 5
            cmd.command=cmdm
    def block1(click,wd,text):
        clicked=click.click-1
        cleanText()
        if clicked==0:
            wd.bgpic('bg\\camp.gif')
            widget()
            write(text[0])
        elif clicked==1:
            cleanText()
            write(text[1])
        else:
            cleanText()
            choice = ['1.Пойти в спортзал.', "2.Пойти в библиотеку.",'3.Выйти на пробежку.']
            ShowChar3(choice[0],choice[1],choice[2])
            if whichChar3(x, y) == 1:
                cmd.command = 1
                click.click2=0
            elif whichChar3(x, y) == 2:
                click.click2 = 0
                cmd.command = 2
            elif whichChar3(x, y) == 3:
                click.click2 = 0
                cmd.command = 3
    def block2(click,wd):
        clicked=click.click-1
        if clicked==0:
            wd.bgpic('bg\\camp.gif')
            cleanText()
            write('Прошло много времени. Пора на вылазку...')
        else:
            cleanText()
            click.noClick()
            click.scenes+=1
            cmd.command=0
            cmd.cmd2 = 0
    if cmd.command==0:
        text=['Хм-м...','Ещё есть время до вылазки. Можно чем-то заняться.']
        block1(click,wd,text)
        cmd.cmd2=4
    elif cmd.command==1:
        workout(click,wd,cmd.cmd2)
    elif cmd.command==2:
        library(click,wd,cmd.cmd2)
    elif cmd.command==3:
        walking(click,wd,cmd.cmd2)
    elif cmd.command==4:
        cmd.cmd2 = 5
        text=['Фух-х-х..','Ещё есть время до вылазки. Можно ещё чем-то заняться.']
        block1(click,wd,text)
    elif cmd.command==5:
        block2(click,wd)
def scene5(click,wd,x,y,gg:MainCharacter,cmd=cmd):
    def block1(click,wd):
        text1=['Леса густые. Леса снежные.','Нужно найти как можно больше ресурсов.','Я могу поохотиться с луком, но дело это непростое. Нужно иметь сильные руки.','Можно ещё пособирать ягоды, но для этого необходимо знать про ядовитые и непитательные виды.','Издалека виднеются заброшенные здания. Если буду достаточно изворотливой, то смогу найти полезные вещи на продажу.']
        clicked=click.click-1
        if clicked==0:
            wd.bgpic('nopic')
            cleanText()
            removeWidjet()
            writeNewChapter('Вылазка.')
        elif clicked==1:
            cleanText()
            wd.bgpic('bg\\woods.gif')
            widget()
            write('...')
        elif 2<=clicked<=5:
            cleanText()
            write(text1[clicked-2])
        else:
            cleanText()
            click.noClick()
            write(text1[clicked-2])
            cmd.command=1
            cmd.cmd2=5
    def block2(click):
        cleanText()
        choice = ['1.Поохотиться на животных.', "2.Пособирать ягоды.", '3.Обыскать заброшки.']
        ShowChar3(choice[0], choice[1], choice[2])
        if whichChar3(x, y) == 1:
            cmd.command = 2
            click.click2 = 0
        elif whichChar3(x, y) == 2:
            click.click2 = 0
            cmd.command = 3
        elif whichChar3(x, y) == 3:
            click.click2 = 0
            cmd.command = 4
    def hunt(click,neededskill,name,cmdm):
        clicked=click.click2-1
        if clicked==0:
            if neededskill<5:
                cleanText()
                write(f'Провал. Недостаточно {name}.')
            else:
                cleanText()
                write(f'Ресурсы собраны.')
                gg.new_balance+=15
        else:
            cleanText()
            click.noClick()
            cmd.command=cmdm
    def block3(click):
        clicked=click.click-1
        if clicked==0:
            cleanText()
            write('Ещё есть время. Можно пособирать ресурсов.')
        else:
            click.noClick()
            click.click2=0
            cmd.command=1
            cmd.cmd2=6
    def block4(click):
        clicked=click.click-1
        text1=['Думаю, на сегодня всё.','Я уже собиралась идти обратно, но вдруг сзади меня зашуршали кусты. ','«Опять чей-то кот?»-подумала я.','Но стоило мне обернуться, и я увидела…','Зомби!!!','Нужно думать быстро, что делать!!!']
        if clicked<len(text1) and clicked!=4:
            cleanText()
            write(text1[clicked])
        elif clicked==4:
            zombie.createZombie(wd)
            widget()
            write(text1[clicked])
        else:
            cleanText()
            choice = ['1.Атаковать и сбежать.', "2.Сразу убежать.", '3.Отвлечь, бросив камень, и убежать.']
            ShowChar3(choice[0], choice[1], choice[2])
            if whichChar3(x, y) == 1:
                cmd.command = 7
                click.click2 = 0
            elif whichChar3(x, y) == 2:
                click.click2 = 0
                cmd.command = 8
            elif whichChar3(x, y) == 3:
                click.click2 = 0
                cmd.command = 9
    def block7(click,towin,char):
        clicked=click.click2-1
        if char>=towin:
            if clicked==0:
                zombie.hidezzz()
                cleanText()
                write('Успех! Ресурсы спасены.')
            else:
                cleanText()
                gg.balance+=gg.new_balance
                gg.new_balance=0
                write('Пора возвращаться домой...')
                click.noClick()
                click.click2=0
                cmd.command=0
                click.scenes+=1
        else:
            if clicked==0:
                cleanText()
                zombie.hidezzz()
                write('Навыков не хватило. Половина ресурсов потеряна.')
            else:
                gg.balance += (gg.new_balance)//2
                gg.new_balance = 0
                cleanText()
                write('Пора возвращаться домой...')
                click.noClick()
                click.click2 = 0
                cmd.command = 0
                click.scenes += 1

    if cmd.command==0:
        block1(click,wd)
    elif cmd.command==1:
        block2(click)
    elif cmd.command==2:
        hunt(click,gg.strength,'силы',cmd.cmd2)
    elif cmd.command==3:
        hunt(click,gg.intelegence,'интелекта',cmd.cmd2)
    elif cmd.command==4:
        hunt(click,gg.dexterity,'ловкости',cmd.cmd2)
    elif cmd.command==5:
        block3(click)
    elif cmd.command==6:
        block4(click)
    elif cmd.command==7:
        twn=zombie.statToBeat
        block7(click,twn,gg.strength)
    elif cmd.command==8:
        twn=zombie.statToBeat
        block7(click,twn,gg.dexterity)
    elif cmd.command==9:
        twn=zombie.statToBeat
        block7(click,twn,gg.intelegence)
def scene6(click,wd,x,y,gg:MainCharacter,cmd=cmd):
    def block1():
        clicked=click.click-1
        text1=['Я сдала все ресурсы, что только могла.','Пока шла сюда заметила ларёк с дешёвыми безделушками.','Думаю, стоит посмотреть подарочки для придурковатых обитателей базы.']
        if clicked<len(text1):
            wd.bgpic('bg\\camp.gif')
            cleanText()
            write(text1[clicked])
        else:
            if clicked==3:
                wd.bgpic('bg\\shop.gif')
                cleanText()
                write('...')
            if clicked>3:
                removeWidjet()
                novel.game.Buy(gg.balance,wd,1)
                if WhichItem(x,y)==1:
                    if gg.balance-30>=0:
                        gg.inventory.append('Цветок')
                        gg.balance-=30
                    else:
                        novel.game.Buy(gg.balance, wd,2)
                elif WhichItem(x,y)==2:
                    if gg.balance-30>=0:
                        gg.inventory.append('Медиатор')
                        gg.balance-=30
                    else:
                        novel.game.Buy(gg.balance, wd, 2)
                elif WhichItem(x,y)==3:
                    if gg.balance-30>=0:
                        gg.inventory.append('Закладка')
                        gg.balance-=30
                    else:
                        novel.game.Buy(gg.balance, wd, 2)
                elif WhichItem(x,y)==4:
                    if gg.balance-50>=0:
                        gg.inventory.append('Сладости')
                        gg.balance-=50
                    else:
                        novel.game.Buy(gg.balance, wd,2)
                elif WhichItem(x,y)==5:
                    click.noClick()
                    click.click2 = 0
                    cmd.command = 1
    def block2():
        clicked=click.click-1
        if clicked==0:
            novel.game.Buy(gg.balance,wd,3)
            novel.game.clearBuy(wd)
            wd.bgpic('bg\\shop.gif')
            widget()
            write('Думаю хватит. Время идти домой.')
        else:
            click.noClick()
            click.click2 = 0
            click.scenes+=1
            cmd.command=0
    if cmd.command==0:
        block1()
    elif cmd.command==1:
        block2()
def scene7(click,wd,x,y,gg:MainCharacter,cmd=cmd):

    def block1():
        clicked=click.click-2
        text=['Как оказалось, в мире апокалипсиса всё не так трагично и энергично.','А главное, тут очень скучно. ','Чтобы скрасить себе дни, я хожу в библиотеку сразу после вылазок.','И снова я тут, Вивьен тоже.','Она вообще выходит на свежий воздух?','Ладно, не важно. Меня ждёт новый том для прочтения!','Художественная литература, как оказалось, не такая уж и скучная.','Я уже прочла кучу книг.','*Несколько часов спустя…*','Я и не заметила, как пролетело время!','Походу, даже Вивьен ушла. Может уже уйти спать?','Мм-м… Может ещё одну главу?','Стоило мне открыть книгу, как я услышала шорох.','Опять этот чёртов шорох!','Оказалось, что слева от меня сидел Вернон.','Я и не заметила его. Походу он сам тоже не заметил меня.','Случайно наши взгляды встретились.']
        if clicked == -1:
            wd.bgpic('nopic')
            wd.bgcolor('white')
            cleanText()
            removeWidjet()
            writeNewChapter('Несколько дней спустя')
        elif clicked<(len(text)-3):
            cleanText()
            wd.bgpic('bg\\library.gif')
            widget()
            write(text[clicked])
        elif 14<=clicked<=15:
            cleanText()
            vernon.showVernon()
            widget()
            write(text[clicked])
        elif clicked==16:
            cleanText()
            write(text[-1])
        elif clicked>16:
            if valerinC.rep>=30:
                click.click2 = 0
                click.noClick()
                cmd.command=1
            elif valerinC.rep>=0:
                click.click2 = 0
                click.noClick()
                cmd.command=2
            else:
                if clicked==17:
                    cleanText()
                    write('Вернон смотрел на меня чуть ли не с ненавистью. Наверное, это из-за натянутых отношений между мной и его сестрой…')
                else:
                    vernon.hideVernon()
                    click.click2 = 0
                    click.noClick()
                    cmd.command = 110
    def block2():
        clicked=click.click2-1
        vert=[2,4,6,7,9,11,12,13,15]
        ggt=[3,8,10,14]
        text=['Вернон смотрел на меня с искренней улыбкой. Может это из-за моих более-менее хороших отношений с его сестрой?','Он резко прервал тишину.',f'Привет, {gg.name}.','Добрый вечер, Вернон. Завлёкся новой книгой?','Угу…','Неловко.','Ты сблизилась с моей сестрой. Знаешь, давно не было людей, которые могли бы вызвать её доверие.','Может дело в том, что Валерин изменилась, но я вижу, что ты сама по себе такая… тихая, приятная?','Спасибо?','Не пойми превратно. Валерин ни с кем не сближалась после трагедии.','Трагедии? Ты про апокалипсис?','Нет, я говорю про то, что произошло три года назад.','Тогда наши родители попали в автокатастрофу и… с тех пор мы одни.','Никто не помогал, Валерин всем занималась сама. Я ценил её и ценю, поэтому, когда я вижу хороших людей, я хочу, чтоб они сближались с сестрой.','Прости, но я не думаю, что Валерин нравится моё общество.','Ещё как нравится! Просто она вредная и недоверчивая. Сестра этого не показывает, но она хочет проводить больше времени с тобой. Поэтому я тебе это говорю. Всё, как всегда, имеет свои истоки. Всё сложнее чем кажется.']
        if clicked==0 or clicked==1 or clicked==5:
            widget()
            write(text[clicked])
        elif clicked in vert:
            widget(vernon.wcolour)
            write(text[clicked])
        elif clicked in ggt:
            widget(gg.colour)
            write(text[clicked])
        elif len(gg.inventory)>0 and clicked>15:
            text2=['Если это и правда так, может мне сделать ей подарок?',' Это будет хорошей возможностью стать ближе!']
            if 16<=clicked<=17:
                widget()
                write(text2[clicked-16])
            else:
                cleanText()
                choice = ['1.Подарить.', "2.Ничего не дарить."]
                ShowChoice(choice[0], choice[1])
                if whichChoice(x, y) == 1:
                    click.button = None
                    cmd.command = 100
                    click.click = 0
                elif whichChoice(x, y) == 2:
                    vernon.hideVernon()
                    click.noClick()
                    cmd.command = 110
        else:
            vernon.hideVernon()
            click.noClick()
            cmd.command = 110
    def block3():
        vernon.hideVernon()
        clicked = click.click - 1
        but = click.button
        removeWidjet()
        cleanText()
        readChar()
        char = readChar(True)
        readInventory()
        invent = readInventory(True)
        if clicked == 0:
            novel.game.Char(char, invent, True)
        if but != None:
            novel.game.RemoveChar()
            if int(but) <= len(gg.inventory):
                item = gg.inventory[int(but) - 1]
                if item in valerinC.favorites:
                    if clicked == 1:
                        widget()
                        write('Вернон посмотрел с любопытством на безделушку.')
                    elif clicked == 2:
                        vernon.showVernon()
                        widget(vernon.wcolour)
                        write('Валерин точно это понравится!')
                    else:
                        vernon.hideVernon()
                        valerinC.rep += 20
                        gg.inventory.pop(int(but) - 1)
                        readChar()
                        click.noClick()
                        cmd.command = 110
                else:
                    if clicked == 1:
                        widget()
                        write('Вернон посмотрел без особого восторга на подарок.')
                    elif clicked == 2:
                        vernon.showVernon()
                        widget(vernon.wcolour)
                        write('Я передам… подарок.')
                    else:
                        vernon.hideVernon()
                        valerinC.rep -= 20
                        readChar()
                        gg.inventory.pop(int(but) - 1)
                        click.noClick()
                        cmd.command = 110
            else:
                if clicked == 1:
                    widget()
                    write('Я решила ничего не дарить.')
                elif clicked == 2:
                    cleanText()
                    click.noClick()
                    cmd.command = 110
    def block110():
        clicked=click.click-1
        if clicked==0:
            widget()
            write('Думаю, самое время идти спатки. Завтра тоже работать.')
        else:
            click.noClick()
            click.click2=0
            cmd.command=5
    def block4():
        clicked=click.click2-1
        text = ['Без интереса на меня посмотрел Вернон и отвернулся.',
                'Походу из-за нейтральных отношений с Валерин я ему безразлична.']
        if 0<=clicked<=1:
            cleanText()
            write(text[clicked])
        elif len(gg.inventory) > 0 and clicked > 1:
            text2 = ['Может через Вернона передать Валерин подарок?', ' Это будет хорошей возможностью стать ближе!']
            if 2 <= clicked <= 3:
                widget()
                write(text2[clicked - 2])
            else:
                cleanText()
                choice = ['1.Подарить.', "2.Ничего не дарить."]
                ShowChoice(choice[0], choice[1])
                if whichChoice(x, y) == 1:
                    click.button = None
                    cmd.command = 100
                    click.click = 0
                elif whichChoice(x, y) == 2:
                    vernon.hideVernon()
                    click.noClick()
                    cmd.command = 110
        else:
            vernon.hideVernon()
            click.noClick()
            cmd.command = 110
    def block5():
        clicked=click.click-1
        if clicked==0:
            cleanText()
            wd.bgpic('nopic')
            removeWidjet()
            writeNewChapter('Несколько недель спустя')
        elif 0<clicked<4:
            cleanText()
            wd.bgpic('bg\\cafitaria.gif')
            text=['Хлоя часто находится в теплице. Она занимается выращиванием овощей и фруктов для пропитания.','Поэтому мы с ней встречаемся только в столовой.','Она постоянно липнет ко мне, говорит о происходящем на базе. ']
            widget()
            write(text[clicked-1])
        else:
            if Cloec.rep>25:
                click.noClick()
                click.click2=0
                cmd.command=6
            elif Cloec.rep>=0:
                click.noClick()
                click.click2 = 0
                cmd.command=7
            elif clicked==4 and Cloec.rep<0:
                cleanText()
                write('Хлоя меня разражает.')
                click.noClick()
                click.click2=0
                cmd.command=220
    def block6():
        clicked=click.click2-1
        clt=[2,4,7,9]
        ggt=[3,8]
        ggthouhgt=[0,5,6,10,11,12]
        text=['Её внимание мне нравится. Поэтому, когда она пригласила меня к себе, я с удовольствие зашла.','Зелень и розовый цвет. Весьма предсказуемо, но мне нравится.',f'{gg.name}, помнишь я рассказывала про фестиваль? Так вот, туда я принесла кексики. Представь, никто не съел ни одного!',
              'Почему?! Ты же так вкусно готовишь!','Наверно я многих отпугивала своим поведением. Они называли меня Барби, сравнивая с куклой. Ведь я такая розовая, добрая и… скучная.','Если так подумать, я сама не лучше.','Я относилась к Хлое предвзято из-за её необычности. Но она точно не скучная, просто другая, разносторонняя.',
              'Знаешь, солнце, мне всё равно что говорят другие. Я всегда буду ценить себя и всё, что имею. Смысл подстраиваться под других, если это скучно?','Ты права. И вообще, ты такая молодец! Быть собой, несмотря ни на что, это дорого стоит.',
              'Ха-ха-ха. Спасибо.','Тишина. Мне она нравится, когда тишина-её молчание.','И вновь болтовня. Мне она тоже нравится, потому что она её.','Захотелось её порадовать.']
        if clicked in ggthouhgt:
            widget()
            write(text[clicked])
        elif clicked in clt:
            widget(Cloec.wcolour)
            write(text[clicked])
        elif clicked in ggt:
            widget(gg.colour)
            write(text[clicked])
        elif clicked==1:
            wd.bgpic("bg\\cloe's.gif")
            Cloec.showCloe()
            cleanText()
            widget()
            write(text[1])
        elif len(gg.inventory)>0 and clicked>12:
            text2='Может сделать подарок?'
            if clicked==12:
                widget()
                write(text2)
            else:
                cleanText()
                choice = ['1.Подарить.', "2.Ничего не дарить."]
                ShowChoice(choice[0], choice[1])
                if whichChoice(x, y) == 1:
                    click.button = None
                    Cloec.hideCloe()
                    cmd.command = 200
                    click.click = 0
                elif whichChoice(x, y) == 2:
                    Cloec.hideCloe()
                    click.noClick()
                    cmd.command = 220
        else:
            Cloec.hideCloe()
            cleanText()
            write('Надо будет купить для неё подарок.')
            click.noClick()
            cmd.command = 220
    def block200():
        clicked = click.click - 1
        but = click.button
        removeWidjet()
        cleanText()
        readChar()
        char = readChar(True)
        readInventory()
        invent = readInventory(True)
        if clicked == 0:
            novel.game.Char(char, invent, True)
        if but != None:
            novel.game.RemoveChar()
            if int(but) <= len(gg.inventory):
                item = gg.inventory[int(but) - 1]
                if item in Cloec.favorites:
                    if clicked == 1:
                        Cloec.showCloe()
                        widget(Cloec.wcolour)
                        write('Это мне?! Спасибо огромное!')
                    else:
                        Cloec.hideCloe()
                        Cloec.rep += 20
                        gg.inventory.pop(int(but) - 1)
                        readChar()
                        click.noClick()
                        cmd.command = 220
                else:
                    if clicked == 1:
                        Cloec.showCloe()
                        widget(Cloec.wcolour)
                        write('Эм-м-м… Спасибо.')
                    else:
                        Cloec.hideCloe()
                        Cloec.rep -= 20
                        readChar()
                        gg.inventory.pop(int(but) - 1)
                        click.noClick()
                        cmd.command = 220
            else:
                if clicked == 1:
                    widget()
                    write('Я решила ничего не дарить.')
                    click.noClick()
                    cmd.command = 220
    def block220():
        cleanText()
        widget()
        Cloec.hideCloe()
        text='Опять Хлоя заболтала меня. Было уже поздно, и я решила убежать домой.'
        clicked=click.click-1
        if clicked==0:
            widget()
            write(text)
        elif clicked==1:
            wd.bgpic('nopic')
            writeNewChapter('Спустя некотрое время...')
            cmd.command=0
            click.noClick()
            click.click2=0
            click.scenes+=1
    def block7():
        text='Может сделать ей подарок?'
        clicked=click.click-1
        if clicked==0:
            widget()
            write(text)
        elif len(gg.inventory) > 0 and clicked>0:
                cleanText()
                choice = ['1.Подарить.', "2.Ничего не дарить."]
                ShowChoice(choice[0], choice[1])
                if whichChoice(x, y) == 1:
                    click.button = None
                    Cloec.hideCloe()
                    cmd.command = 200
                    click.click = 0
                elif whichChoice(x, y) == 2:
                    Cloec.hideCloe()
                    click.noClick()
                    cmd.command = 220
        else:
            Cloec.hideCloe()
            cleanText()
            write('Надо будет купить для неё подарок.')
            click.noClick()
            cmd.command = 220
    if cmd.command==0:
        block1()
    elif cmd.command==1:
        block2()
    elif cmd.command==100:
        block3()
    elif cmd.command==2:
        block4()
    elif cmd.command==110:
        block110()
    elif cmd.command==5:
        block5()
    elif cmd.command==6:
        block6()
    elif cmd.command==200:
        block200()
    elif cmd.command==7:
        block7()
    elif cmd.command==220:
        block220()
def scene8(click,wd,x,y,gg:MainCharacter,cmd=cmd):
    def block1():
        cleanText()
        clicked = click.click
        text1 = ['Пора идти на вылазку. ', 'Снова я вышла из безопасного лагеря.',
                 'В лесах Сеула меня может поджидать всë что угодно.',
                 'И в этот раз это был не кот, не озверевшая белка, а... ', 'Араши! ', 'И рядом с ним... ',
                 'Зомби!!! ', 'Да что же это такое!']
        if clicked<=3:
            wd.bgpic('bg\\woods.gif')
            cleanText()
            write(text1[clicked])
        elif clicked==4:
            Arashic.createSpriteArashi(wd)
            # Arashic.showArashi()
            widget()
            write(text1[clicked])
        elif clicked==5:
            Arashic.hideArashi()
            cleanText()
            write(text1[clicked])
        elif clicked==6:
            zombie.createZombie(wd)
            widget()
            write(text1[clicked])
        elif clicked==7:
            cleanText()
            write(text1[clicked])
        else:
            if Arashic.rep>=20:
                zombie.hidezzz()
                click.click2=0
                click.noClick()
                cmd.command=101
            elif Arashic.rep>=0:
                zombie.hidezzz()
                click.click2 = 0
                click.noClick()
                cmd.command=102
            else:
                zombie.hidezzz()
                click.click2 = 0
                click.noClick()
                cmd.command=200
    def block101():
        clicked=click.click2-1
        ggt=[0,1,2,3,4,5,11,12,15,16,20,21,22,23,27]
        av=[6,8,9,17,18,24,26]
        ggv=[7,10,13,14,19,25]
        text2=['На один лишь миг, но Араши посмотрел на меня с глазами, полными страха.','Впервые я видела его таким... ','Не раздумывая, я подбежала к Араши, схватила за руку и быстро помогла встать. ','И мы бежали. Долго бежали. ','Сражаться с зомби бессмысленно, поэтому побег-единственный выход.',
               'Кое-как отдышавшись, мы посмотрели друг на друга.',f'Спасибо, {Arashic.mcName}.','Та не за что! Как я могла бы оставить тебя одного.','Поверь, многие бы так и поступили на твоëм месте.','Зачем рисковать своей жизнью ради кого-то другого?','Потому что в моей глупой голове таится мысль о том, что если я помогу другим, то и они мне тоже.',
                'Молчание.','Ветерок сотрясает его помпезную прическу. Кстати о ней...','Забавно, твоя укладка держится даже после произошедшего.','Ха-ха-ха.','Теперь не Араши злорадствовал, а я вредно улыбалась.','Это и впрямь приятно! Надо будет практиковать чаще.','Ага, она переживёт всех нас.',
               'А теперь лучше обсудить путь обратно... ','М-м-м. Нужно идти на север. Мы оттуда бежали.','Так мы и пошли.','... Долгая дорога.','Как мы так далеко убежали?','Араши неловко стоял возле входа в лагерь. Я же собиралась на вылазку.','Ты всё равно идёшь на вылазку? ',
               'А что тебя удивляет? Зомби во время апокалипсиса?','Да не то чтобы. Ладно, тебе лучше знать. ','Походу он сильно испугался.']
        if clicked==5:
            wd.bgpic('bg\\field.gif')
        if clicked==22:
            wd.bgpic('bg\\camp.gif')
        if clicked==20:
            Arashic.hideArashi()
        if clicked in ggt:
            widget()
            write(text2[clicked])
        elif clicked in av:
            Arashic.showArashi()
            widget(Arashic.wcolour)
            write(text2[clicked])
        elif clicked in ggv:
            widget(gg.colour)
            write(text2[clicked])
        else:
            if len(gg.inventory)>0 and clicked>27:
                if cliked==28:
                    cleanText()
                    write('Может подарить ему чего-нибудь?')
            elif clicked==29:
                cleanText()
                choice = ['1.Подарить.', "2.Ничего не дарить."]
                ShowChoice(choice[0], choice[1])
                if whichChoice(x, y) == 1:
                    click.button = None
                    cmd.command = 111
                    click.click = 0
                elif whichChoice(x, y) == 2:
                    Arashic.hideArashi()
                    click.noClick()
                    cmd.command = 200
    if cmd.command==0:
        block1()
    if cmd.command==101:
        block101()