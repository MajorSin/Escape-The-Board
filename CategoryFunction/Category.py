import Router
import json

class Category():
    chosen_category = ''
    hovered = False
    
    def prep(self):
        global json_file
        json_file = open('questions.json')
        
        global questions
        questions = json.loads(json_file.read())
    
        global category_font
        category_font = createFont("fonts/american-captain.otf", 120)
        
        global font
        font = createFont('Arial', 70)
        
        global return_image
        return_image = loadImage("images/left-arrow.png")
        return_image.resize(110, 128)
        
        global return_image_hovered
        return_image_hovered = loadImage("images/left-arrow-hovered.png")
        return_image_hovered.resize(110, 128)
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        textFont(category_font)
        stroke(0)
        strokeWeight(10)
        
        if chosen_category == 'Standard':
            fill('#2d42ab')
            rect(0, 0, 1000, 200)
            fill(255)
            text('Standaard', 450, 145)
        elif chosen_category == 'Knowledge':
            fill('#640700')
            rect(0, 0, 1000, 200)
            fill(255)
            text('Kennis', 640, 145)
        else:
            fill('#123900')
            rect(0, 0, 1000, 200)
            fill(255)
            text('Wiskunde', 510, 145)
        
        fill(100)
        stroke(100)
        rect(40, 40, 330, 120, 15)
        
        if self.hovered:
            image(return_image_hovered, 50, 40)
        else:
            image(return_image, 50, 40)
        
        fill(Category.mouse_over(self))
        textFont(font)
        text('Terug', 175, 123)
        
        fill(255)
        text('Vragen uit categorie:', 180, 350)
        textSize(35)
        
        temp = 450
        temp_id = 1
        if chosen_category == 'Standard':
            for question in questions:
                text(str(temp_id) + ': ' + question['question'], 180, temp)
                temp += 100
                temp_id += 1
        else:
            temp_category = chosen_category
            
            if chosen_category == 'Knowledge':
                temp_category = 'kennis'
            elif chosen_category == 'Math':
                temp_category = 'wiskunde'
                
            for question in questions:
                if question['category'] == temp_category:
                    text(str(temp_id) + ': ' + question['question'], 180, temp)
                    temp += 100
                    temp_id += 1
        
        Category.check(self)
    
    def check(self):
        Category.mouse_over(self)
        
    def mouse_over(self):
        if (40 <= mouseX <= 370) and (40 <= mouseY <= 160):
            self.hovered = True
            return '#00f1fe'
        else:
            self.hovered = False
            return '#ffffff'
    
    def set_category(self, category):
        global chosen_category
        chosen_category = category
        
    def mousePressed(self):
        if (40 <= mouseX <= 370) and (40 <= mouseY <= 160):
            Router.set_screen('')
