import Router
import InterfaceMain

class InterFace():
    hovered_start = False
    hovered_add = False
    hovered_exit = False
    
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
        
        global startknop_hovered
        startknop_hovered = loadImage("images/start-hover.png")
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        background(main_background)
        image(logo, 550, 10, 200, 220)
        
        textFont(evil32)
        textSize(70)
        fill(250,250,250)
        text("Escape The Board", 415,320)
        
        if self.hovered_start:
            image(startknop_hovered, 403, 370, 476, 120)
        else:
            image(startknop, 403, 370, 476, 120)

        textFont(bungee32)
        
        if self.hovered_add:
            fill('#00f1fe')
        else:
            fill("#AEAEAE")
            
        text("Vraag Invoeren", 489,570)
        
        if self.hovered_exit:
            fill('#00f1fe')
        else:
            fill("#FF686B")
            
        text("EXIT", 596,640)

        textSize(25)
        fill(250,250,250)
        text("Team 4", 1150,700)
        
        InterFace.check(self)
    
    def check(self):
        InterFace.mouse_hover(self)
        
    def mouse_hover(self):
        start_l = (403 <= mouseX <= 879) and (370 <= mouseY <= 480)
        question_input_l = (489 <= mouseX <= 789) and (530 <= mouseY <= 580)
        exit_l = (596 <= mouseX <= 686) and (600 <= mouseY <= 650)
        
        if start_l:
            self.hovered_start = True
        elif question_input_l:
            self.hovered_add = True
        elif exit_l:
            self.hovered_exit = True
        else:
            self.hovered_start = False
            self.hovered_add = False
            self.hovered_exit = False
            
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
