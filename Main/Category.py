import UserInputMain, CategoryMain
import Router

class Category():
    chosen_category = ''
    hovered_question = False
    hovered_obstacle = False
    hovered_return = False
    hovered_yes = False
    hovered_no = False
    hovered_restart = False
    reset_enabled = False
    game_finished = False
    
    def __init__(self, leaderboard, category_question, obstakel):
        self.leaderboard = leaderboard
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
        
        if self.reset_enabled:
            fill(50)
            rect(250, 200, 780, 420)
            fill(255)
            textSize(70)
            text('Weet je het zeker?', 390, 300)
            
            stroke(50)
            textSize(70)
            
            if self.hovered_yes:
                fill('#00cc2d')
            else:
                fill('#00a023')
                
            rect(320, 400, 300, 150)
            
            fill(255)
            text('Verder', 380, 500)
            
            if self.hovered_no:
                fill('#cc1a1a')
            else:
                fill('#9f1414')
            rect(660, 400, 300, 150)
            
            textSize(55)
            fill(255)
            text('Herstarten', 695, 495)
            
            stroke(0)
        elif self.category_question.out_of_questions:
            fill(50)
            rect(250, 200, 780, 420)
            fill(255)
            textSize(60)
            text('Er zijn geen vragen meer', 350, 300)
            
            stroke(100)
            fill(100)
            rect(480, 400, 300, 100)
            
            if self.hovered_restart:
                fill('#00f1fe')
            else:
                fill('#bcbcbc')
                    
            text('Resetten', 535, 470)
        
        users = self.leaderboard.user_list
        for user in users:
            if user.score >= 20:
                self.game_finished = True
        
        if self.game_finished:
            fill(50)
            rect(250, 200, 780, 420)
            fill(255)
            textSize(60)
            for user in users:
                if user.score >= 20:
                    if user.id == 1:
                        fill('#D26466')
                    elif user.id == 2:
                        fill('#A7C7E7')
                    elif user.id == 3:
                        fill('#77dd77')
                    else:
                        fill('#FDFD96')
                    text('Speler ' + str(user.id) + ': ' + user.name, 493, 300)
                    fill(255)
                    text('Heeft het spel gewonnen!', 350, 370)
            stroke(50)
            textSize(70)
            
            if self.hovered_yes:
                fill('#00cc2d')
            else:
                fill('#00a023')
                
            rect(320, 400, 300, 150)
            
            fill(255)
            text('Exit', 415, 500)
            
            if self.hovered_no:
                fill('#cc1a1a')
            else:
                fill('#9f1414')
                
            rect(660, 400, 300, 150)
            textSize(55)
            fill(255)
            text('Herstarten', 695, 495)
            
        stroke(0)
                
        #Houdt alle onderdelen in check bij.
        Category.check(self)
    
    #Verantwoordelijk voor controleren.
    def check(self):
        Category.mouse_over(self)
        
    #Mouse hover wordt hier bijgehouden.
    def mouse_over(self):
        mouse_x = 110 <= mouseX <= 710
        
        if mouse_x and (200 <= mouseY <= 470) and not(self.reset_enabled or self.category_question.out_of_questions or self.game_finished):
            self.hovered_question = True
            self.hovered_obstacle = False
        elif mouse_x and (500 <= mouseY <= 680) and not(self.reset_enabled or self.category_question.out_of_questions or self.game_finished):
            self.hovered_obstacle = True
            self.hovered_question = False
        elif (40 <= mouseX <= 260) and (25 <= mouseY <= 145) and not(self.reset_enabled or self.category_question.out_of_questions or self.game_finished):
            self.hovered_return = True
        elif (320 <= mouseX <= 620) and (400 <= mouseY <= 550) and (self.reset_enabled or self.game_finished):
            self.hovered_yes = True
        elif (660 <= mouseX <= 960) and (400 <= mouseY <= 550) and (self.reset_enabled or self.game_finished):
            self.hovered_no = True
        elif (480 <= mouseX <= 780) and (400 <= mouseY <= 500) and self.category_question.out_of_questions:
            self.hovered_restart = True
        else:
            self.hovered_question = False
            self.hovered_obstacle = False
            self.hovered_return = False
            self.hovered_yes = False
            self.hovered_no = False
            self.hovered_restart = False
    
    #Categorie wordt hierdoor aangepast.
    def set_category(self, category):
        self.chosen_category = category
        
    def mousePressed(self):
        mouse_x = 110 <= mouseX <= 710
        
        #Vraag scherm wordt hierdoor getoond.
        if mouse_x and (200 <= mouseY <= 470) and not(self.reset_enabled or self.category_question.out_of_questions or self.game_finished):
            self.reset_enabled = False
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
        elif mouse_x and (500 <= mouseY <= 800) and not(self.reset_enabled or self.category_question.out_of_questions or self.game_finished):
            Router.set_screen('Obstakel')
            category = ''
            if self.chosen_category == 'Standard':
                category = 'Standaard'
            elif self.chosen_category == 'Knowledge':
                category = 'Kennis'
            else:
                category = 'Wiskunde'
                
            self.obstakel.set_obstakel(category)
        elif (40 <= mouseX <= 260) and (25 <= mouseY <= 145) and not(self.category_question.out_of_questions):
            self.reset_enabled = True
        elif (320 <= mouseX <= 620) and (400 <= mouseY <= 550) and self.reset_enabled:
            self.reset_enabled = False
        elif (320 <= mouseX <= 620) and (400 <= mouseY <= 550) and self.game_finished:
            self.game_finished = False
            exit()
        elif (660 <= mouseX <= 960) and (400 <= mouseY <= 550) and self.reset_enabled:
            self.reset_enabled = False
            Router.set_screen('UserInputMain')
            UserInputMain.reset_players()
            CategoryMain.reset_questions()
        elif (660 <= mouseX <= 960) and (400 <= mouseY <= 550) and self.game_finished:
            self.game_finished = False
            Router.set_screen('UserInputMain')
            UserInputMain.reset_players()
            CategoryMain.reset_questions()
        elif (480 <= mouseX <= 780) and (400 <= mouseY <= 500) and self.category_question.out_of_questions:
            CategoryMain.set_screen('Categories')
            CategoryMain.reset_questions()
            self.category_question.out_of_questions = False
