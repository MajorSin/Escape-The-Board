import json

from obstakelmoeilijk import *
moeilijkobstakel = moeilijkobstakel()
from tegenstander import *
tegenstander = tegenstander()
from tweegoed import *
tweegoed = tweegoed()

#standaard variable
keuze = "none"
category = "wiskunde"

#SETUP
def setup():
    global bgImg
    global bungee32
    global logo
    global segoe50
    size(1280,720)
    bgImg = loadImage("img/achtergrond.jpg")
    background(bgImg)
    noStroke()
    bungee32 = createFont("data/Bungee-Regular.ttf", 32)
    segoe50 = createFont("Segoe UI Bold", 50)
    logo = loadImage("img/Skelet.png")
    
def draw():
    #GEEN OBSTAKEL GESELECTEERD
    textFont(segoe50)
    fill(250,250,250)
    if keuze == "none":
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
        text("Klik links op een obstakel", 350,190)
    #OBSTAKEL MOEILIJK VRAAG
    elif keuze == "moeilijk":
        pass
    #OBSTAKEL 2 GOED
    elif keuze == "tweegoed":
        pass
    #TEGENSTANDER
    elif keuze == "tegenstander":
        pass
    
def mousePressed():
    #GLOBAL VAR
    global keuze
    #ANNULEER
    pass
    #MOEILIJK OBSTAKEL
    if 0 < mouseX < 220 and 70 < mouseY < 70 + 220:
        keuze = "moeilijk"
        moeilijkobstakel.display(category)
        moeilijkobstakel.obstakel(category)
    #TWEE GOED OBSTAKEL
    elif 0 < mouseX < 220 and 300 < mouseY < 300 + 220:
        keuze = "tweegoed"
        tweegoed.display(category)
        tweegoed.obstakel(category)
    #VRAAG TEGENSTANDER OBSTAKEL
    elif 0 < mouseX < 220 and 300 < mouseY < 520 + 220:
        keuze = "tegenstander"
        tegenstander.display(category)
        tegenstander.obstakel(category)
    #MOEILIJK MOUSEPRESSED
    if keuze == 'moeilijk':
        moeilijkobstakel.mousePressed()
    elif keuze == 'tegenstander':
        tegenstander.mousePressed()
        moeilijkobstakel.mousePressed()
    elif keuze == 'tweegoed':
        tweegoed.mousePressed()
