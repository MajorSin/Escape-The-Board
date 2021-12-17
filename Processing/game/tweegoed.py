import json
import random

used_makkelijk = []

class tweegoed():
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
        global index2
        global main2
        textFont(createFont("data/Bungee-Regular.ttf", 20))
        fill(250,250,250)
        index_random = []
        json_file = open('json/questions.json')
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
            #VRAAG 1
            index = random.choice(index_random)
            main = data[index]
            text("1: " + main['question'],270,150)
            #MTP
            if main['type'] == "mtp":
                fill('#f56600')
                circle(277, 190, 40)
                circle(607, 190, 40)
                circle(937, 190, 40)
                fill(250,250,250)
                text("A    " + str(main['A']),270,197)
                text("B    " + str(main['B']),600,197)
                text("C    " + str(main['C']),930,197)
            #VRAAG 2
            index2 = random.choice(index_random)
            while index2 == index:
                index2 = random.choice(index_random)
            main2 = data[index2]
            text("2: " + main2['question'],270,250)
            #MTP
            if main2['type'] == "mtp":
                fill('#f56600')
                circle(277, 290, 40)
                circle(607, 290, 40)
                circle(937, 290, 40)
                fill(250,250,250)
                text("A    " + str(main2['A']),270,297)
                text("B    " + str(main2['B']),600,297)
                text("C    " + str(main2['C']),930,297)
            #ANTWOORD 
            textSize(25)
            fill("#f56600")
            rect(270,360,545,70)
            fill(100, 0, 53)
            text("Laat beide antwoorden zien", 330, 400)
        except:
            text("Er zijn geen vragen meer!",400,150)
            
    #LAAT ANTWOORD ZIEN
    def antwoord(self):
        textFont(createFont("data/Bungee-Regular.ttf", 30))
        fill(250,250,250)
        used_makkelijk.append(index)
        used_makkelijk.append(index2)
        textSize(25)
        text("1: " + str(main['answer']), 270, 460)
        text("2: " + str(main2['answer']), 270, 500)
        
    #MOUSEPRESSED
    def mousePressed(self):
        #ANTWOORD LATEN ZIEN
        if 270 < mouseX < 270 + 545 and 360 < mouseY < 360 + 70:
            self.antwoord()
