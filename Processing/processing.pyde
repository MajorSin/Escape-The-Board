#IMPORT FILES
from moeilijkObstakel import *
from tweegoed import *
from tegenstander import *

#IMPORT CLAS
moeilijkObstakel = moeilijkObstakel()
tweegoedObstakel = tweegoedObstakel()
tegenstanderObstakel = tegenstanderObstakel()

#STANDARD VARIABLES
category = "standaard"
basisObstakel = True
moeilijk = False
tweegoed = False
tegenstander = False

def setup():
    global bgImg
    global bgVImg
    global evil32
    global logo
    size(1280,720)
    bgImg = loadImage("img/achtergrond.jpg")
    bgVImg = loadImage("img/Vachtergrond.jpg")
    noStroke()
    evil32 = createFont("data/Evil_Empire.otf", 32)
    logo = loadImage("img/Skelet.png")
    
def draw():
    global basisObstakel
    #BASIS OBSTAKEL SCHERM
    if basisObstakel:
        #SETUP
        noStroke()
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
    
def mousePressed():
    global moeilijk
    global tweegoed
    global tegenstander
    global basisObstakel
    #MOEILIJK VRAAG OBSTAKEL KNOP
    if 0 < mouseX < 0 + 200 and 120 < mouseY < 120 + 200:
        moeilijk = True
        tweegoed = False
        tegenstander = False
        basisObstakel = False
        moeilijkObstakel.display(category)
        moeilijkObstakel.inhoud(category)
    #TWEE GOED OBSTAKEL KNOP
    elif 0 < mouseX < 0 + 200 and 340 < mouseY < 340 + 200:
        moeilijk = False
        tegenstander = False
        tweegoed = True
        basisObstakel = False
        tweegoedObstakel.display(category)
        tweegoedObstakel.inhoud(category)
    #TEGENSTNDER
    elif 0 < mouseX < 0 + 200 and 540 < mouseY < 540 + 200:
        moeilijk = False
        tegenstander = True
        tweegoed = False
        basisObstakel = False
        tegenstanderObstakel.display(category)
        tegenstanderObstakel.inhoud(category)
    #MOEILIJK OBSTAKEL
    if moeilijk:
        moeilijkObstakel.mousePressed()
    elif tweegoed:
        tweegoedObstakel.mousePressed()
    elif tegenstander:
        tegenstanderObstakel.mousePressed()
