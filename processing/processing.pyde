#IMPORT FILES
from vraag import *

#IMPORT CLAS
vraag = vraag()

#STANDARD VARIABLES
vraagButton = False

def setup():
    global bgImg
    global evil32
    global logo
    size(1280,720)
    bgImg = loadImage("img/achtergrond.jpg")
    background(bgImg)
    noStroke()
    evil32 = createFont("data/Evil_Empire.otf", 32)
    logo = loadImage("img/Skelet.png")
    
def draw():
    #VRAAG KNOP
    if vraagButton:
        pass
    #BASISSCHERM
    else:
        #SETUP
        global category
        noStroke()
        background(bgImg)
        category = "wiskunde"
        if category == "standaard":
            headercolor = "#2D42AB"
        elif category == "kennis":
            headercolor = "#640700"
        elif category == "wiskunde":
            headercolor = "#123900"
        #HEADER
        textFont(evil32)
        textSize(65)
        fill(headercolor)
        rect(0, 0, 754, 150)
        fill(250, 250, 250)
        text(category, 400, 95)
        #GA TERUG
        textFont(createFont("Segoe UI Bold", 32))
        fill("#978787")
        rect(20, 10, 200, 130, 28)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",52,85)
        #MAKKELIJK KNOP
        fill(0, 0, 0)
        rect(81,190,592,322)
        fill(250, 250, 250)
        textFont(evil32)
        textSize(50)
        text("Pik een vraag",244,475)
        image(logo, 290, 220, 180, 197)
        #OBSTAKEL KNOP
        fill(0, 0, 0)
        rect(81,540,592,140)
        fill(250, 250, 250)
        text("Obstakel",310,605)
        text("melden",325,650)
        image(logo, 202, 560, 85, 97)
    
def mousePressed():
    global vraagButton
    #MAKKELIJKE VRAAG BUTTONS
    if 81 < mouseX < 81 + 592 and 190 < mouseY < 190 + 322 and vraagButton == False:
        vraagButton = True
        vraag.display(vraag, category)
    #IN VRAAG.PY
    elif vraagButton == True:
        vraag.mousePressed(vraagButton)
    #ANNULEER 
    if 55 < mouseX < 55 + 150 and 45 < mouseY < 45 + 50 and vraagButton == True:
        vraagButton = False
