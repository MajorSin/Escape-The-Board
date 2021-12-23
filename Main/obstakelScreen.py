from moeilijkObstakel import *
moeilijkObstakel = moeilijkObstakel()
from tweegoed import *
tweeGoed =tweeGoed()
from tegenstander import *
tegenstander = tegenstander()

import Router, json, random, sys, CategoryMain
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
    goedKnop = False
    current_user = 0
    user_list = []
    
    def prep(self):
        global bgVImg
        bgVImg = loadImage("images/Vachtergrond.jpg")

        global font
        font = createFont("Segoe UI Bold", 40)
        
        global moeilijk_picture
        moeilijk_picture = loadImage("images/moeilijk_obstakel.png")
        
        global twee_goed_picture
        twee_goed_picture = loadImage("images/2goed_obstakel.png")
        
        global tegenstander_picture
        tegenstander_picture = loadImage("images/tegenstander_obstakel.png")
        
        global bungee33
        bungee33 = createFont("fonts/bungee-regular.ttf", 33)
        
        global bungee22
        bungee22 = createFont("fonts/bungee-regular.ttf", 22)
                
    def display(self):
        noStroke()
        background(bgVImg)
        #ANNULEER
        fill(100)
        rect(60, 20, 250, 80)
        fill(250, 250, 250)
        textSize(32)
        
        #CATEGORIE
        textFont(font)
        textSize(50)
        text('Annuleer', 77, 75)
        fill('#bcbcbc')
        if current_category == 'Standaard':
            text('Categorie: ' + current_category.capitalize(), 710, 70)
        elif current_category == 'Kennis':
            text('Categorie: ' + current_category.capitalize(), 820, 70)
        else:
            text('Categorie: ' + current_category.capitalize(), 710, 70)
            
        #LAAT OBSTAKEL KNOPPEN ZIEN
        image(moeilijk_picture,0,120,200,200)
        image(twee_goed_picture,0,340,200,200)
        image(tegenstander_picture,-10,540,200,200)
        
        textFont(bungee33)
        if self.basisObstakel:
            text("Klik links op een obstakel", 400, 200)
        elif self.moeilijk:
            if main == 'empty':
                text("Er zijn geen vragen meer!",400,150)
            else:
                textFont(bungee22)
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
                textFont(bungee22)
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
                textFont(bungee22)
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
        #VRAAG GOED KNOP
        if self.goedKnop:
            fill('#00a023')
            rect(1000, 500, 200, 100)
            fill(0)
            if self.tweegoed:
                text('VRAGEN \n   GOED', 1035, 543)
            else:
                text('VRAAG \n  GOED', 1040, 543)
                
        textFont(font)
        textSize(30)
        
        id = self.current_user
        if id == 1:
            fill('#D26466')
        elif id == 2:
            fill('#A7C7E7')
        elif id == 3:
            fill('#77dd77')
        else:
            fill('#FDFD96')
        
        users = self.user_list
        name = ''
        for user in users:
            if user.id == id:
                name = user.name
                
        text('Speler ' + str(self.current_user) + ': ' + str(name) + ' ' + 'is aan de beurt', 430, 690)
    
    def prepare_player(self):
        leaderboard = CategoryMain.get_leaderboard()
        self.current_user = leaderboard.current_user
        self.user_list = leaderboard.user_list
                                        
    def set_obstakel(self, category):
        global current_category
        current_category = category
    
    #MOUSE CLICK
    def mousePressed(self):
        global moeilijk
        global main
        global main2
        global goedKnop
        #MOEILIJK VRAAG OBSTAKEL KNOP
        if 0 < mouseX < 0 + 200 and 120 < mouseY < 120 + 200:
            self.moeilijk = True
            self.tweegoed = False
            self.tweeAntwoord = False
            self.tegenstander = False
            self.tegenstanderAntwoord = False
            self.basisObstakel = False
            self.moeilijkAntwoord = False
            self.goedKnop = False
            main = moeilijkObstakel.inhoud(current_category)
        #TWEE GOED OBSTAKEL KNOP
        elif 0 < mouseX < 0 + 200 and 340 < mouseY < 340 + 200:
            self.moeilijk = False
            self.tweegoed = True
            self.tweeAntwoord = False
            self.tegenstander = False
            self.tegenstanderAntwoord = False
            self.moeilijkAntwoord = False
            self.basisObstakel = False
            self.goedKnop = False
            main = tweeGoed.vraagEen(current_category)
            main2 = tweeGoed.vraagTwee(current_category)
        #VRAAG AAN TEGENSTANDER KNOP
        elif 0 < mouseX < 0 + 200 and 540 < mouseY < 540 + 200:
            self.moeilijk = False
            self.tweegoed = False
            self.tweeAntwoord = False
            self.tegenstander = True
            self.tegenstanderAntwoord = False
            self.moeilijkAntwoord = False
            self.basisObstakel = False
            self.goedKnop = False
            main = tegenstander.vraag(current_category)
        #MOEILIJK VRAAG ANWOORD
        if 240 < mouseX < 240 + 475 and 290 < mouseY < 290 + 100 and self.moeilijk == True:
            self.moeilijkAntwoord = True
            moeilijkObstakel.antwoord()
            self.goedKnop = True
        #TWEE VRAGEN ANTWOORD
        elif 240 < mouseX < 240 + 475 and 290 < mouseY < 290 + 100 and self.tweegoed == True:
            self.tweeAntwoord = True
            tweeGoed.antwoord()
            self.goedKnop = True
        #VRAAG AAN TEGENSTANDER ANTWOORD
        elif 240 < mouseX < 240 + 475 and 290 < mouseY < 290 + 100 and self.tegenstander == True:
            self.tegenstanderAntwoord = True
            tegenstander.antwoord()
            self.goedKnop = True
        #ANNULEER KNOP
        if 60 < mouseX < 60 + 250 and 20 < mouseY < 20+80:
            leaderboard = CategoryMain.get_leaderboard()
            if self.moeilijk:
                for user in self.user_list:
                    if user.id == self.current_user:
                        if not(user.score == 0):
                            if user.score == 1:
                                user.score -=1
                            else:
                                user.score -=2
            leaderboard.next_user()
            self.show_answer = False
            Router.set_screen('CategoryMain')
            self.moeilijk = False
            self.tweegoed = False
            self.tegenstander = False
            self.basisObstakel = True
        #GOEDKNOP
        if (1000 <= mouseX <= 1200) and (500 <= mouseY <= 600) and self.goedKnop == True:
            leaderboard = CategoryMain.get_leaderboard()
            if self.moeilijk:
                for user in self.user_list:
                    if user.id == self.current_user:
                        user.score += 3
            leaderboard.next_user()
            self.show_answer = False
            Router.set_screen('CategoryMain')
            self.moeilijk = False
            self.tweegoed = False
            self.tegenstander = False
            self.goedKnop = False
            self.basisObstakel = True
