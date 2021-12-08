import json
# AANPASSINGEN: GA TERUG KNOP
from get import *
from post import *
from reset import *

get = get()
post = post()
reset = reset()

buttonPressedGetVragen = False
buttonPressedVraagInvoegen = False
errorScreenInput = False
buttonPressedResetten1 = False
buttonPressedResetten2 = False

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def setup():
    #BACKGROUND
    global bgImg
    global evil32
    size(1280,720)
    bgImg = loadImage("img/achtergrond.jpg")
    background(bgImg)
    #FONT
    evil32 = createFont("data/Evil_Empire.otf", 32)

def draw():
    textFont(evil32)
    #AANVRAAG VRAGEN
    if buttonPressedGetVragen:
        #get.set()
        True
    #BUTTON OM INVOEGEN
    elif buttonPressedVraagInvoegen:
        #post.set()
        post.display(vraag, antwoord, category, graad)
    #RESETTEN VRAGEN
    elif buttonPressedResetten1:
        pass
    #ERROR SCREEN INPUT
    elif errorScreenInput:
        background(bgImg)
        #GA TERUG
        textFont(createFont("Segoe UI Bold", 32))
        fill("#978787")
        rect(20, 10, 200, 130, 28)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",52,85)
        #ERROR TEXT
        textSize(40)
        fill(255, 255, 255)
        text("ERROR",570,80)
        textSize(18)
        text("Input is leeg of u heeft ergens een typefout gemaakt",410,120)
    else:
        #BASISSCHERM
        noStroke()
        textSize(50)
        background(bgImg)
        #ALLE VRAGEN OPHALEN
        fill("#2D42AB")
        rect(156.5,180,967,114.15)
        fill(255, 255, 255)
        text("TOEGEVOEGDE VRAGEN ZIEN",399,255)
        #VRAGEN TOEVOEGEN
        fill("#123900")
        rect(156.5,330,967,114.15)
        fill(255, 255, 255)
        text("VRAAG TOEVOEGEN",477,405)
        #ALLES RESETTEN
        fill("#640700")
        rect(156.5,480,967,114.15)
        fill(255, 255, 255)
        text("TOEGEVOEGDE VRAGEN VERWIJDEREN",307,550)
        #HEADER
        header = loadImage("img/header.png")
        image(header, 265, 10, 750, 130)
        #GA TERUG
        textFont(createFont("Segoe UI Bold", 32))
        fill("#978787")
        rect(20, 10, 200, 130, 28)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",52,85)
        
def mousePressed():
    global buttonPressedGetVragen
    global buttonPressedVraagInvoegen
    global buttonPressedResetten1
    global buttonPressedResetten2
    global antwoord
    global vraag
    global antwoord
    global category
    global errorScreenInput
    global graad
    #BUTTON VOOR RUNNEN
    if 156.5 < mouseX < 156.5 + 967 and 180 < mouseY < 180 + 114.15 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == False:
        buttonPressedGetVragen = True
        get.display()
    #BUTTON VOOR INVOEGEN
    elif 156.5 < mouseX < 156.5 + 967 and 330 < mouseY < 330 + 114.15 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == False:
        #WELKE VRAAG TOEVOEGEN
        vraag = input('Welk vraag wilt u invoegen (kan niet leeg)?')
        #VRAAG LEGE INPUT
        if vraag == "" or vraag == " ":
            errorScreenInput = True
        #VRAAG VOLLEDIG
        elif vraag:
            #ANTWOORD INDIENEN
            antwoord = input('Wat is het antwoord (kan niet leeg)?')
            #ANTWOORD LEGE INPUT
            if antwoord == "" or antwoord == " ":
                errorScreenInput = True
            #ANTWOORD VOLLEDIG
            elif antwoord:
                #CATEGORIE INDIENEN
                category = input('In welk categorie? (kennis of wiskunde)?').lower()
                #CATEGORIE LEGE INPUT
                if category == "" or category == " ":
                    errorScreenInput = True
                #NIET GOED GEKOZEN
                elif category != 'kennis'and category != "wiskunde":
                    errorScreenInput = True
                #CATEGORIE VOLLEDIG
                elif category == 'kennis' or category == "wiskunde":
                    graad = input('Welk moeilijkheidsgraad? (moeilijk of makkelijk)?').lower()
                    #VRAAG LEGE INPUT
                    if graad == "" or graad == " ":
                        errorScreenInput = True
                    #NIET GOED GEKOZEN
                    elif graad != 'moeilijk'and graad != "makkelijk":
                        errorScreenInput = True
                    #GRAAD VOLLEDIG
                    elif graad == 'moeilijk' or graad == "makkelijk":
                        post.append(vraag, antwoord, category, graad)
                        buttonPressedVraagInvoegen = True
                    #ANNULERING = TERUGBRENGEN
                    else:
                        buttonPressedVraagInvoegen = False
                #ANNULERING = TERUGBRENGEN
                else:
                    buttonPressedVraagInvoegen = False
            #ANNULERING = TERUGBRENGEN
            else:
                buttonPressedVraagInvoegen = False
        #ANNULERING = TERUGBRENGEN
        else:
            buttonPressedVraagInvoegen = False
    #BUTTON VOOR RESETTEN VRAGEN
    elif 156.5 < mouseX < 156.5 + 967 and 480 < mouseY < 480 + 114.15 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == False:
        buttonPressedResetten1 = True
        reset.display(buttonPressedResetten2)
    #BUTTON VOOR BEVESTIGING RESETTEN VRAAG
    elif 415 < mouseX < 415 + 450 and 205 < mouseY < 205 + 100 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == True:
        buttonPressedResetten2 = True
        reset.reset2()
    #GA TERUG
    if 20 < mouseX < 20 + 200 and 10 < mouseY < 10 + 130:
        buttonPressedGetVragen = False
        buttonPressedVraagInvoegen = False
        errorScreenInput = False
        buttonPressedResetten1 = False
        buttonPressedResetten2 = False
