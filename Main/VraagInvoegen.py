import json
from get import *
from post import *
from reset import *
import Router
get = get()
post = post()
reset = reset()

class VraagInvoegen():
    x = 5
    
    buttonPressedGetVragen = False
    buttonPressedVraagInvoegen = False
    errorScreenInput = False
    buttonPressedResetten1 = False
    buttonPressedResetten2 = False

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def prep(self):
        global evil32
        evil32 = createFont("fonts/evil-empire.otf", 32)

    def display(self):
        textFont(evil32)
        #AANVRAAG VRAGEN
        if self.buttonPressedGetVragen:
            #get.set()
            True
            get.display()
        #BUTTON OM INVOEGEN
        elif self.buttonPressedVraagInvoegen:
            #post.set()
            post.display(vraag, antwoord, category, graad)
            pass
        #RESETTEN VRAGEN
        elif self.buttonPressedResetten1:
            pass
            reset.display()
        #ERROR SCREEN INPUT
        elif self.errorScreenInput:
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
            bgImg = loadImage("images/main-background.jpg")
            background(bgImg)
            noStroke()
            textSize(50)
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
            header = loadImage("images/header.png")
            image(header, 265, 10, 750, 130)
            #GA TERUG
            textFont(createFont("Segoe UI Bold", 32))
            fill("#978787")
            rect(20, 10, 200, 130, 28)
            textSize(32)
            fill(100, 0, 53)
            text("Ga Terug",52,85)
        
    def mousePressed(self):
        global antwoord
        global vraag
        global antwoord
        global category
        global graad
        
        #BUTTON VOOR RUNNEN
        if 156.5 < mouseX < 156.5 + 967 and 180 < mouseY < 180 + 114.15 and self.buttonPressedGetVragen == False and self.buttonPressedVraagInvoegen == False and self.buttonPressedResetten1 == False:
            self.buttonPressedGetVragen = True
            get.display()
        #BUTTON VOOR INVOEGEN
        elif 156.5 < mouseX < 156.5 + 967 and 330 < mouseY < 330 + 114.15 and self.buttonPressedGetVragen == False and self.buttonPressedVraagInvoegen == False and self.buttonPressedResetten1 == False:
            #WELKE VRAAG TOEVOEGEN
            vraag = self.input('Welk vraag wilt u invoegen (kan niet leeg)?')
            #VRAAG LEGE INPUT
            if vraag == "" or vraag == " ":
                self.errorScreenInput = True
            #VRAAG VOLLEDIG
            elif vraag:
                #ANTWOORD INDIENEN
                antwoord = self.input('Wat is het antwoord (kan niet leeg)?')
                #ANTWOORD LEGE INPUT
                if antwoord == "" or antwoord == " ":
                    self.errorScreenInput = True
                #ANTWOORD VOLLEDIG
                elif antwoord:
                    #CATEGORIE INDIENEN
                    category = self.input('In welk categorie? (kennis of wiskunde)?').lower()
                    #CATEGORIE LEGE INPUT
                    if category == "" or category == " ":
                        self.errorScreenInput = True
                    #NIET GOED GEKOZEN
                    elif category != 'kennis'and category != "wiskunde":
                        self.errorScreenInput = True
                    #CATEGORIE VOLLEDIG
                    elif category == 'kennis' or category == "wiskunde":
                        graad = self.input('Welk moeilijkheidsgraad? (moeilijk of makkelijk)?').lower()
                        #VRAAG LEGE INPUT
                        if graad == "" or graad == " ":
                            self.errorScreenInput = True
                        #NIET GOED GEKOZEN
                        elif graad != 'moeilijk'and graad != "makkelijk":
                            self.errorScreenInput = True
                        #GRAAD VOLLEDIG
                        elif graad == 'moeilijk' or graad == "makkelijk":
                            post.append(vraag, antwoord, category, graad)
                            self.buttonPressedVraagInvoegen = True
                        #ANNULERING = TERUGBRENGEN
                        else:
                            self.buttonPressedVraagInvoegen = False
                    #ANNULERING = TERUGBRENGEN
                    else:
                        self.buttonPressedVraagInvoegen = False
                #ANNULERING = TERUGBRENGEN
                else:
                    self.buttonPressedVraagInvoegen = False
            #ANNULERING = TERUGBRENGEN
            else:
                self.buttonPressedVraagInvoegen = False
        #BUTTON VOOR RESETTEN VRAGEN
        elif 156.5 < mouseX < 156.5 + 967 and 480 < mouseY < 480 + 114.15 and self.buttonPressedGetVragen == False and self.buttonPressedVraagInvoegen == False and self.buttonPressedResetten1 == False:
            self.buttonPressedResetten1 = True
            reset.display()
        #BUTTON VOOR BEVESTIGING RESETTEN VRAAG
        elif 415 < mouseX < 415 + 450 and 205 < mouseY < 205 + 100 and self.buttonPressedGetVragen == False and self.buttonPressedVraagInvoegen == False and self.buttonPressedResetten1 == True:
            self.buttonPressedResetten2 = True
            reset.reset2()
        #GA TERUG
        if 20 < mouseX < 20 + 200 and 10 < mouseY < 10 + 130 and self.buttonPressedGetVragen == False and self.buttonPressedVraagInvoegen == False and self.buttonPressedResetten1 == False and self.errorScreenInput == False and self.buttonPressedResetten2 == False:
            Router.set_screen('InterfaceMain')
            self.buttonPressedGetVragen = False
            self.buttonPressedVraagInvoegen = False
            self.errorScreenInput = False
            self.buttonPressedResetten1 = False
            self.buttonPressedResetten2 = False
        #GA TERUG
        elif 20 < mouseX < 20 + 200 and 10 < mouseY < 10 + 130:
            self.buttonPressedGetVragen = False
            self.buttonPressedVraagInvoegen = False
            self.errorScreenInput = False
            self.buttonPressedResetten1 = False
            self.buttonPressedResetten2 = False
