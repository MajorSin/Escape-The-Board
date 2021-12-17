import json
import random

used_moeilijk = []

class moeilijkobstakel():
    #DISPLAY
    def display(self,category):
        bgImg = loadImage("img/achtergrond.jpg")
        bungee32 = createFont("data/Bungee-Regular.ttf", 32)
        segoe50 = createFont("Segoe UI Bold", 50)
        background(bgImg)
        textFont(bungee32)
        textSize(50)
        fill("#e5ff00")
        #ANNULEER
        text("Annuleer",10,50)
        #CATEGORY
        if category == "kennis":
            text("Type: " + category, 900,50)
        elif category == "standaard":
            text("Type: " + category, 780,50)
        elif category == "wiskunde":
            text("Type: " + category, 820,50)
        #IMAGE OBSTAKELS
        moeilijk = loadImage("img/moeilijk_obstakel.png")
        image(moeilijk, 0,70,220,220)
        tweegoed = loadImage("img/2goed_obstakel.png")
        image(tweegoed, 0,300,220,220)
        tegenstander = loadImage("img/tegenstander_obstakel.png")
        image(tegenstander, -10,520,220,220)
        textFont(segoe50)
        fill(250,250,250)
    
    #LAAT VRAAG ZIEN
    def obstakel(self, category):
        global main
        global index
        textFont(createFont("data/Bungee-Regular.ttf", 20))
        fill(250,250,250)
        index_random = []
        json_file = open('json/questions.json')
        data = json.loads(json_file.read())
        for i in range(len(data)):
            main = data[i]
            if category == "standaard":
                if main['level'] == "moeilijk":
                    if i not in used_moeilijk:
                        index_random.append(i)
            elif main['level'] == "moeilijk" and main['category'] == category:
                if i not in used_moeilijk:
                    index_random.append(i)
        try:
            index = random.choice(index_random)
            main = data[index]
            text(main['question'],270,150)
            #MTP
            if main['type'] == "mtp":
                fill('#f56600')
                circle(277, 217, 40)
                circle(607, 217, 40)
                circle(937, 217, 40)
                fill(250,250,250)
                text("A    " + str(main['A']),270,225)
                text("B    " + str(main['B']),600,225)
                text("C    " + str(main['C']),930,225)
            #ANTWOORD 
            textSize(25)
            fill("#f56600")
            rect(270,290,475,100)
            fill(100, 0, 53)
            text("Laat antwoord zien", 350, 350)
        except:
            text("Er zijn geen vragen meer!",400,150)
            
    #LAAT ANTWOORD ZIEN
    def antwoord(self):
        textFont(createFont("data/Bungee-Regular.ttf", 30))
        fill(250,250,250)
        used_moeilijk.append(index)
        text(main['answer'], 270, 450)
        
    #MOUSEPRESSED
    def mousePressed(self):
        #ANTWOORD LATEN ZIEN
        if 270 < mouseX < 270 + 475 and 290 < mouseY < 290 + 100:
            self.antwoord()
