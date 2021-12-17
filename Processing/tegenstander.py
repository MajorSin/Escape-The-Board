import json
import random

used_makkelijk = []

class tegenstanderObstakel():
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
        global index
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
            main = data[index]
            text(main['question'],250,150)
            #MTP
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
        except:
            text("Er zijn geen vragen meer!",400,150)
            
    #LAAT ANTWOORD ZIEN
    def antwoord(self):
        fill(250,250,250)
        used_makkelijk.append(index)
        text(main['answer'], 240, 430)
        
    #MOUSEPRESSED
    def mousePressed(self):
        #ANTWOORD LATEN ZIEN
        if 240 < mouseX < 240 + 570 and 340 < mouseY < 340 + 100:
            self.antwoord()
