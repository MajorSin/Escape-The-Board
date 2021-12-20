import Router
import InterfaceMain

class InterFace():
    def prep(self):
        #Laadt de afbeeldingen in.
        global main_background
        main_background = loadImage("images/main-background.jpg")
        
        global logo
        logo = loadImage("images/skull.png")
        
        global evil32
        evil32 = createFont("fonts/evil-empire.otf", 32)
        
        global bungee32
        bungee32 = createFont("fonts/bungee-regular.ttf", 32)
        
        global startknop
        startknop = loadImage("images/start.png")
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        main_background = loadImage("images/main-background.jpg")
        background(main_background)
        image(logo, 550, 10, 200, 220)
        
        textFont(evil32)
        textSize(70)
        fill(250,250,250)
        text("Escape The Board", 415,320)
    
        image(startknop, 403, 370, 476, 120)

        textFont(bungee32)
        fill("#AEAEAE")
        text("Vraag Invoeren", 489,570)

        fill("#FF686B")
        text("EXIT", 596,640)

        textSize(25)
        fill(250,250,250)
        text("Team 4", 1150,700)
        
    def mousePressed(self):
        #Locatie op de x en y van de knoppen.
        start_l = (403 <= mouseX <= 879) and (370 <= mouseY <= 480)
        question_input_l = (489 <= mouseX <= 789) and (530 <= mouseY <= 580)
        exit_l = (596 <= mouseX <= 686) and (600 <= mouseY <= 650)
        
        #Zorgt dat functies worden uitgevoert als een knop is geklikt.
        if start_l and Router.current_screen == 'InterfaceMain':
            Router.set_screen('UserInputMain')
        elif question_input_l:
            Router.set_screen('QuestionInput')
        elif exit_l:
            exit()
