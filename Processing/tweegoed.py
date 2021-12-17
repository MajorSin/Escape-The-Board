import json
import random

used_makkelijk = []

class tweegoedObstakel():
    #DISPLAY
    def display(self, category):
        #SETUP
        noStroke()
        bgVImg = loadImage("img/Vachtergrond.jpg")
        background(bgVImg)
        #ANNULEER
        fill(250, 250, 250)
        textFont(createFont("Segoe UI Bold", 25))
        textSize(32)
        text("Annuleer",55,75)
        #CATEGORIE
        text("Categorie: " + category.capitalize(),900,75)
        #LAAT OBSTAKEL KNOPPEN ZIEN
        moeilijk = loadImage("img/moeilijk_obstakel.png")
        image(moeilijk,0,120,200,200)
        tweegoed = loadImage("img/2goed_obstakel.png")
        image(tweegoed,0,340,200,200)
        tegenstander = loadImage("img/tegenstander_obstakel.png")
        image(tegenstander,-10,540,200,200)
    
    #LAAT VRAAG ZIEN
    def inhoud(self, category):
        global main
        global main2
        global index
        global index2
        textFont(createFont("data/Bungee-Regular.ttf", 22))
        fill(250,250,250)
        index_random = []
        json_file = open('questions.json')
        data = json.loads(json_file.read())
        for i in range(len(data)):
            main = data[i]
            if category == "standaard":
                if main['level'] == "makkelijk":
                    if i not in used_makkelijk:
                        index_random.append(i)
            elif main['level'] == "makkelijk" and main['category'] == category:
                if i not in used_makkelijk:
                    index_random.append(i)
        try:
            index = random.choice(index_random)
            index2 = random.choice(index_random)
            while index == index2:
                index2 = random.choice(index_random)
            main = data[index]
            main2 = data[index2]
            text("1: " + main['question'],250,150)
            text("2: " + main2['question'],250,260)
            #MTP
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
        except:
            text("Er zijn geen vragen meer!",400,150)
            
    #LAAT ANTWOORD ZIEN
    def antwoord(self):
        fill(250,250,250)
        used_makkelijk.append(index)
        used_makkelijk.append(index2)
        text(main['answer'], 240, 455)
        text(main2['answer'], 240, 485)
        
    #MOUSEPRESSED
    def mousePressed(self):
        #ANTWOORD LATEN ZIEN
        if 240 < mouseX < 240 + 570 and 340 < mouseY < 340 + 80:
            self.antwoord()
