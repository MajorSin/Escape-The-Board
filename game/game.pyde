#IMPORT
import json

#STANDARD VARIABLES
startscherm = True
vraagInvoegen = False

buttonPressedGetVragen = False
buttonPressedVraagInvoegen = False
errorScreenInput = False
buttonPressedResetten1 = False
buttonPressedResetten2 = False

#VRAAG INVOEREN IMPORT
from vraaginvoegen import *
vraaginvoegen = vraaginvoegen()
from get import *
get = get()
from post import *
post = post()
from reset import *
reset = reset()

#SETUP
def setup():
    global logo
    global evil32
    global bungee32
    global startknop
    global bgImg
    size(1280,720)
    bgImg = loadImage("img/achtergrond.jpg")
    background(bgImg)
    noStroke()
    logo = loadImage("img/Skelet.png")
    evil32 = createFont("data/Evil_Empire.otf", 32)
    bungee32 = createFont("data/Bungee-Regular.ttf", 32)
    startknop = loadImage("img/Start knop.png")
    
def draw():
    if startscherm:
        background(bgImg)
        #LOGO
        image(logo,550,10,200,220)
        #ESCAPE THE BOARD
        textFont(evil32)
        textSize(70)
        fill(250,250,250)
        text("Escape The Board", 415,320)
        #START KNOP
        image(startknop,403,370,476,120) #3,97
        textFont(bungee32)
        #VRAAG INVOEREN EN EXIT
        fill("#AEAEAE")
        text("Vraag Invoeren", 489,570)
        fill("#FF686B")
        text("EXIT", 596,640)
        #TEAM 4
        textSize(25)
        fill(250,250,250)
        text("Team 4", 1150,700)
    elif vraagInvoegen:
        vraaginvoegen.setup(buttonPressedGetVragen, buttonPressedVraagInvoegen, errorScreenInput, buttonPressedResetten1, buttonPressedResetten2)
        
        
def mousePressed():
    #BUTTON GLOBAL VAR
    global startscherm
    global vraagInvoegen
    #-----------------------------------
    #VRAAG INVOEREN
    #-----------------------------------
    #STANDARD VAR
    global buttonPressedGetVragen
    global buttonPressedVraagInvoegen
    global errorScreenInput
    global buttonPressedResetten1
    global buttonPressedResetten2
    #-----------------------------------
    #STARTSCHERM
    #-----------------------------------
    #EXIT AFTER PRESSED ON EXIT
    if 590 < mouseX < 590 + 100 and 610 < mouseY < 610 + 40 and vraagInvoegen == False and startscherm == True:
        exit()
    #VRAAG INVOEREN
    elif startscherm and 490 < mouseX < 490 + 310 and 540 < mouseY < 540 + 40 and vraagInvoegen == False and startscherm == True:
        startscherm = False
        vraagInvoegen = True
    #-----------------------------------
    #VRAAG INVOEREN
    #-----------------------------------
    #TERUG NAAR START
    elif 20 < mouseX < 20 + 200 and 10 < mouseY < 10 + 130 and vraagInvoegen == True and startscherm == False:
        startscherm = True
        vraagInvoegen = False
    #KRIJG OVERZICHT VRAGEN
    elif 156.5 < mouseX < 156.5 + 967 and 180 < mouseY < 180 + 114.15 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == False and vraagInvoegen == True:
        vraagInvoegen = False
        buttonPressedGetVragen = True 
        get.display()
    #EEN VRAAG TOEVOEGEN
    elif 156.5 < mouseX < 156.5 + 967 and 330 < mouseY < 330 + 114.15 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == False and vraagInvoegen == True:
        #WELKE VRAAG TOEVOEGEN
        vraag = vraaginvoegen.input('Welk vraag wilt u invoegen (kan niet leeg)?')
        #VRAAG LEGE INPUT
        if vraag == "" or vraag == " ":
            errorScreenInput = True
        #VRAAG VOLLEDIG
        elif vraag:
            #ANTWOORD INDIENEN
            antwoord = vraaginvoegen.input('Wat is het antwoord (kan niet leeg)?')
            #ANTWOORD LEGE INPUT
            if antwoord == "" or antwoord == " ":
                errorScreenInput = True
            #ANTWOORD VOLLEDIG
            elif antwoord:
                #CATEGORIE INDIENEN
                category = vraaginvoegen.input('In welk categorie? (kennis of wiskunde)?').lower()
                #CATEGORIE LEGE INPUT
                if category == "" or category == " ":
                    errorScreenInput = True
                #NIET GOED GEKOZEN
                elif category != 'kennis'and category != "wiskunde":
                    errorScreenInput = True
                #CATEGORIE VOLLEDIG
                elif category == 'kennis' or category == "wiskunde":
                    graad = vraaginvoegen.input('Welk moeilijkheidsgraad? (moeilijk of makkelijk)?').lower()
                    #VRAAG LEGE INPUT
                    if graad == "" or graad == " ":
                        errorScreenInput = True
                    #NIET GOED GEKOZEN
                    elif graad != 'moeilijk'and graad != "makkelijk":
                        errorScreenInput = True
                    #GRAAD VOLLEDIG
                    elif graad == 'moeilijk' or graad == "makkelijk":
                        post.append(vraag, antwoord, category, graad)
                        post.display(vraag, antwoord, category, graad)
                        vraagInvoegen = False
                        startscherm = False
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
    #VRAGEN RESETTEN
    elif 156.5 < mouseX < 156.5 + 967 and 480 < mouseY < 480 + 114.15 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == False and vraagInvoegen == True:
        buttonPressedResetten1 = True
        vraagInvoegen = False
        reset.display()
    #VRAGEN RESETTEN BEVESTIGING
    elif 415 < mouseX < 415 + 450 and 205 < mouseY < 205 + 100 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and vraagInvoegen == False and startscherm == False and buttonPressedResetten1 == True:
        reset.reset2()
    elif 20 < mouseX < 20 + 200 and 10 < mouseY < 10 + 130 and vraagInvoegen == False and startscherm == False and (buttonPressedGetVragen == True or buttonPressedVraagInvoegen == True or buttonPressedResetten1 == True):
        vraagInvoegen = True
        buttonPressedGetVragen = False
        buttonPressedVraagInvoegen = False
        buttonPressedResetten1 = False
        
