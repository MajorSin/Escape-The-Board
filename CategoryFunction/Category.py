import Router

class Category():
    chosen_category = ''
    hovered_question = False
    hovered_obstacle = False
    
    def __init__(self, category_question):
        self.category_question = category_question
        
    #Gereed stellen wat nodig is.
    def prep(self):
        global category_background
        category_background = loadImage("images/category-background.jpg")
        
        global category_font
        category_font = createFont("fonts/evil-empire.otf", 100)
    
        global skull_image_question
        skull_image_question = loadImage("images/skull.png")
        skull_image_question.resize(160, 160)
        
        global skull_image_obstacle
        skull_image_obstacle = loadImage("images/skull.png")
        skull_image_obstacle.resize(140, 140)
        
        global font
        font = createFont('Segoe UI Bold', 70)
        
        global leaderboard_image
        leaderboard_image = loadImage("images/leaderboard.png")
        leaderboard_image.resize(170, 170)
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        tint(255)
        background(category_background)
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
        
        fill(0)
        rect(800, 0, 480, 280)
        
        fill('#00f1fe')
        circle(1040, 100, 140)
        image(leaderboard_image, 953, 10)
        
        textFont(font)
        textSize(60)
        text('LEADERBOARD', 825, 250)
        
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
            
        text('OBSTAKEL \n  MELDEN', 320, 570
             )    
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
        else:
            self.hovered_question = False
            self.hovered_obstacle = False
    
    #Categorie wordt hierdoor aangepast.
    def set_category(self, category):
        self.chosen_category = category
        
    def mousePressed(self):
        mouse_x = 110 <= mouseX <= 710
        
        #Vraag scherm wordt hierdoor getoond.
        if mouse_x and (200 <= mouseY <= 470):
            Router.set_screen('Question')
            category = ''
            
            if self.chosen_category == 'Standard':
                category = 'Standaard'
            elif self.chosen_category == 'Knowledge':
                category = 'Kennis'
            else:
                category = 'Wiskunde'
            
            self.category_question.prepare_question(category)
            
            
        
