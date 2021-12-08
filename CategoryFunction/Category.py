import Router
import json

class Category():
    chosen_category = ''
    
    def prep(self):
        # global json_file
        # json_file = open('questions.json')
        
        # global questions
        # questions = json.loads(json_file.read())
    
        global category_font
        category_font = createFont("fonts/evil-empire.otf", 100)
        
        global font
        font = createFont('Segoe UI Bold', 70)
        
        global leaderboard_image
        leaderboard_image = loadImage("images/leaderboard.png")
        leaderboard_image.resize(170, 170)
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        textFont(category_font)
        stroke(0)
        strokeWeight(10)
        
        if chosen_category == 'Standard':
            fill('#2d42ab')
            rect(0, 0, 800, 170)
            fill(255)
            text('Standaard', 330, 120)
        elif chosen_category == 'Knowledge':
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
        
        # temp = 450
        # temp_id = 1
        # if chosen_category == 'Standard':
        #     for question in questions:
        #         text(str(temp_id) + ': ' + question['question'], 180, temp)
        #         temp += 100
        #         temp_id += 1
        # else:
        #     temp_category = chosen_category
            
        #     if chosen_category == 'Knowledge':
        #         temp_category = 'kennis'
        #     elif chosen_category == 'Math':
        #         temp_category = 'wiskunde'
                
        #     for question in questions:
        #         if question['category'] == temp_category:
        #             text(str(temp_id) + ': ' + question['question'], 180, temp)
        #             temp += 100
        #             temp_id += 1
        
        #Category.check(self)
    
    # def check(self):
    #     Category.mouse_over(self)
        
    # def mouse_over(self):
    #     if (40 <= mouseX <= 370) and (40 <= mouseY <= 160):
    #         self.hovered = True
    #         return '#00f1fe'
    #     else:
    #         self.hovered = False
    #         return '#ffffff'
    
    def set_category(self, category):
        global chosen_category
        chosen_category = category
        
    def mousePressed(self):
        if (40 <= mouseX <= 370) and (40 <= mouseY <= 160):
            Router.set_screen('')
