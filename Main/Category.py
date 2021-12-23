import UserInputMain, CategoryMain
import Router

class Category():
    chosen_category = ''
    hovered_question = False
    hovered_obstacle = False
    hovered_return = False
    
    def __init__(self, category_question, obstakel):
        self.category_question = category_question
        self.obstakel = obstakel
        
    #Gereed stellen wat nodig is.
    def prep(self):
        global main_background
        main_background = loadImage("images/main-background.jpg")
        
        global category_font
        category_font = createFont("fonts/evil-empire.otf", 100)
    
        global skull_image_question
        skull_image_question = loadImage("images/skull.png")
        skull_image_question.resize(160, 160)
        
        global skull_image_obstacle
        skull_image_obstacle = loadImage("images/skull.png")
        skull_image_obstacle.resize(140, 140)
        
        global bungee32
        bungee32 = createFont("fonts/bungee-regular.ttf", 32)
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        tint(255)
        background(main_background)
        textFont(category_font)
        stroke(0)
        strokeWeight(10)
        
        #Houdt bij welke categorie gekozen is.
        if self.chosen_category == 'Standard':
            fill('#2d42ab')
            rect(0, 0, 800, 170)
            fill(255)
            text('Standaard', 330, 120)
        elif self.chosen_category == 'Knowledge':
            fill('#640700')
            rect(0, 0, 800, 170)
            fill(255)
            text('Kennis', 480, 120)
        else:
            fill('#123900')
            rect(0, 0, 800, 170)
            fill(255)
            text('Wiskunde', 360, 120)
        
        fill(100)
        stroke(100)
        rect(40, 25, 220, 120, 15)
        
        if self.hovered_return:
            fill('#00f1fe')
        else:
            fill(255)
        
        textFont(bungee32)
        textSize(40)
        text('Herstart', 40.3, 100)
        
        stroke(0)
        fill(0)
        rect(110, 200, 600, 270)
        
        image(skull_image_question, 330, 210)
   
        if self.hovered_question:
            fill('#00f1fe')
        else:
            fill(255)
            
        textFont(category_font)
        textSize(70)
        text('KIES EEN VRAAG', 215, 450)
        
        fill(0)
        rect(110, 500, 600, 180)
        
        image(skull_image_obstacle, 150, 520)
        
        if self.hovered_obstacle:
            fill('#00f1fe')
        else:
            fill(255)
            
        text('OBSTAKEL \n  MELDEN', 320, 570)

        #Houdt alle onderdelen in check bij.
        Category.check(self)
    
    #Verantwoordelijk voor controleren.
    def check(self):
        Category.mouse_over(self)
        
    #Mouse hover wordt hier bijgehouden.
    def mouse_over(self):
        mouse_x = 110 <= mouseX <= 710
        
        if mouse_x and (200 <= mouseY <= 470):
            self.hovered_question = True
        elif mouse_x and (500 <= mouseY <= 680):
            self.hovered_obstacle = True
        elif (40 <= mouseX <= 260) and (25 <= mouseY <= 145):
            self.hovered_return = True
        else:
            self.hovered_question = False
            self.hovered_obstacle = False
            self.hovered_return = False
    
    #Categorie wordt hierdoor aangepast.
    def set_category(self, category):
        self.chosen_category = category
        
    def mousePressed(self):
        mouse_x = 110 <= mouseX <= 710
        
        #Vraag scherm wordt hierdoor getoond.
        if mouse_x and (200 <= mouseY <= 470):
            CategoryMain.set_screen('Question')
            category = ''
            
            if self.chosen_category == 'Standard':
                category = 'Standaard'
            elif self.chosen_category == 'Knowledge':
                category = 'Kennis'
            else:
                category = 'Wiskunde'
            
            self.category_question.prepare_question(category)
        #OBSTAKEL SCHERM WORDT HIER GETOOND
        elif mouse_x and (500 <= mouseY <= 800):
            Router.set_screen('Obstakel')
            category = ''
            if self.chosen_category == 'Standard':
                category = 'Standaard'
            elif self.chosen_category == 'Knowledge':
                category = 'Kennis'
            else:
                category = 'Wiskunde'
                
            self.obstakel.set_obstakel(category)
        elif (40 <= mouseX <= 260) and (25 <= mouseY <= 145):
            Router.set_screen('UserInputMain')
            UserInputMain.reset_players()
