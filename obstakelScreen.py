from moeilijkObstakel import *
moeilijkObstakel = moeilijkObstakel()
from tweegoed import *
tweeGoed =tweeGoed()
from tegenstander import *
tegenstander = tegenstander()

import Router
import json
import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class obstakel():
    current_category = ''
    basisObstakel = True
    moeilijk = False
    moeilijkAntwoord = False
    tweegoed = False
    tweeAntwoord = False
    tegenstander = False
    tegenstanderAntwoord = False
    
    def display(self):
        bgVImg = loadImage("images/Vachtergrond.jpg")
        noStroke()
        background(bgVImg)
        #ANNULEER
        fill(100)
        rect(60, 20, 250, 80)
        fill(250, 250, 250)
        textFont(createFont("Segoe UI Bold", 25))
        textSize(32)
        #CATEGORIE
        subold = createFont('Segoe UI Bold', 40)
        textFont(subold)
        textSize(50)
        text('Annuleer', 77, 75)
        fill('#bcbcbc')
        if self.current_category == 'Standaard':
            text('Categorie: ' + self.current_category.capitalize(), 710, 70)
        elif self.current_category == 'Kennis':
            text('Categorie: ' + self.current_category.capitalize(), 820, 70)
        else:
            text('Categorie: ' + self.current_category.capitalize(), 710, 70)
        #LAAT OBSTAKEL KNOPPEN ZIEN
        moeilijk = loadImage("images/moeilijk_obstakel.png")
        image(moeilijk,0,120,200,200)
        tweegoed = loadImage("images/2goed_obstakel.png")
        image(tweegoed,0,340,200,200)
        tegenstander = loadImage("images/tegenstander_obstakel.png")
        image(tegenstander,-10,540,200,200)
        textFont(createFont("fonts/Bungee-Regular.ttf", 33))
        if self.basisObstakel:
            text("Klik links op een obstakel", 400, 200)
        elif self.moeilijk:
            if main == 'empty':
                text("Er zijn geen vragen meer!",400,150)
            else:
                textFont(createFont("fonts/Bungee-Regular.ttf", 22))
                fill(250,250,250)
                text(main['question'],250,150)
                if main['type'] == "mtp":
                    fill('#f56600')
                    circle(258, 218, 40)
                    circle(627, 218, 40)
                    circle(996, 218, 40)
                    fill(250,250,250)
                    text("A    " + str(main['A']),250,225)
                    text("B    " + str(main['B']),620,225)
                    text("C    " + str(main['C']),990,225)
                #ANTWOORD 
                textSize(30)
                fill("#f56600")
                rect(240,290,475,100)
                fill(100, 0, 53)
                text("Laat antwoord zien", 300, 350)
                if self.moeilijkAntwoord == True:
                    fill(250,250,250)
                    text(main['answer'], 240, 430)
        elif self.tweegoed:
            if main == 'empty' or main2 == 'empty':
                text("Er zijn geen vragen meer!",400,150)
            else:
                textFont(createFont("fonts/Bungee-Regular.ttf", 22))
                fill(250,250,250)
                text("1: " + main['question'],250,150)
                text("2: " + main2['question'],250,260)
                if main['type'] == "mtp":
                    fill('#f56600')
                    circle(258, 190, 40)
                    circle(627, 190, 40)
                    circle(996, 190, 40)
                    fill(250,250,250)
                    text("A    " + str(main['A']),250,197)
                    text("B    " + str(main['B']),620,197)
                    text("C    " + str(main['C']),990,197)
                if main2['type'] == "mtp":
                    fill('#f56600')
                    circle(258, 300, 40)
                    circle(627, 300, 40)
                    circle(996, 300, 40)
                    fill(250,250,250)
                    text("A    " + str(main2['A']),250,307)
                    text("B    " + str(main2['B']),620,307)
                    text("C    " + str(main2['C']),990,307)
                #ANTWOORD
                textSize(30)
                fill("#f56600")
                rect(240,340,570,80)
                fill(100, 0, 53)
                text("Laat beide antwoorden zien", 270, 390)
                if self.tweeAntwoord == True:
                    fill(250,250,250)
                    text(main['answer'], 240, 455)
                    text(main2['answer'], 240, 485)
        elif self.tegenstander:
            if main == 'empty':
                text("Er zijn geen vragen meer!",400,150)
            else:
                textFont(createFont("fonts/Bungee-Regular.ttf", 22))
                fill(250,250,250)
                text(main['question'],250,150)
                if main['type'] == "mtp":
                    fill('#f56600')
                    circle(258, 218, 40)
                    circle(627, 218, 40)
                    circle(996, 218, 40)
                    fill(250,250,250)
                    text("A    " + str(main['A']),250,225)
                    text("B    " + str(main['B']),620,225)
                    text("C    " + str(main['C']),990,225)
                #ANTWOORD 
                textSize(30)
                fill("#f56600")
                rect(240,290,475,100)
                fill(100, 0, 53)
                text("Laat antwoord zien", 300, 350)
                if self.tegenstanderAntwoord == True:
                    fill(250,250,250)
                    text(main['answer'], 240, 430)
        
    def set_obstakel(self, category):
        self.current_category = category
    
    #MOUSE CLICK
    def mousePressed(self):
        global moeilijk
        global main
        global main2
        #MOEILIJK VRAAG OBSTAKEL KNOP
        if 0 < mouseX < 0 + 200 and 120 < mouseY < 120 + 200:
            self.moeilijk = True
            self.tweegoed = False
            self.tweeAntwoord = False
            self.tegenstander = False
            self.tegenstanderAntwoord = False
            self.basisObstakel = False
            self.moeilijkAntwoord = False
            main = moeilijkObstakel.inhoud(self.current_category)
        #TWEE GOED OBSTAKEL KNOP
        elif 0 < mouseX < 0 + 200 and 340 < mouseY < 340 + 200:
            self.moeilijk = False
            self.tweegoed = True
            self.tweeAntwoord = False
            self.tegenstander = False
            self.tegenstanderAntwoord = False
            self.moeilijkAntwoord = False
            self.basisObstakel = False
            main = tweeGoed.vraagEen(self.current_category)
            main2 = tweeGoed.vraagTwee(self.current_category)
        #VRAAG AAN TEGENSTANDER KNOP
        elif 0 < mouseX < 0 + 200 and 540 < mouseY < 540 + 200:
            self.moeilijk = False
            self.tweegoed = False
            self.tweeAntwoord = False
            self.tegenstander = True
            self.tegenstanderAntwoord = False
            self.moeilijkAntwoord = False
            self.basisObstakel = False
            main = tegenstander.vraag(self.current_category)
        #MOEILIJK VRAAG ANWOORD
        if 240 < mouseX < 240 + 475 and 290 < mouseY < 290 + 100 and self.moeilijk == True:
            self.moeilijkAntwoord = True
            moeilijkObstakel.antwoord()
        #TWEE VRAGEN ANTWOORD
        elif 240 < mouseX < 240 + 475 and 290 < mouseY < 290 + 100 and self.tweegoed == True:
            self.tweeAntwoord = True
            tweeGoed.antwoord()
        #VRAAG AAN TEGENSTANDER ANTWOORD
        elif 240 < mouseX < 240 + 475 and 290 < mouseY < 290 + 100 and self.tegenstander == True:
            self.tegenstanderAntwoord = True
            tegenstander.antwoord()
        #ANNULEER KNOP
        if 60 < mouseX < 60 + 250 and 20 < mouseY < 20+80:
            self.show_answer = False
            Router.set_screen('Category')
            self.moeilijk = False
            self.tweegoed = False
            self.tegenstander = False
            self.basisObstakel = True
