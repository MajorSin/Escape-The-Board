import Router
import json
import random

class CategoryQuestion():
    question = []
    current_category = ''
    hovered_cancel = False
    
    #Gereed stellen wat nodig is.
    def prep(self):
        global json_file
        json_file = open('questions.json')
        
        global questions
        questions = json.loads(json_file.read())
    
        global category_background
        category_background = loadImage("images/category-background.jpg")
        
        global font
        font = createFont('Segoe UI Bold', 40)
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        tint(100)
        image(category_background, 0, 0)
        
        fill(100)
        rect(60, 20, 250, 80)
        
        if self.hovered_cancel:
            fill('#00f1fe')
        else:
            fill('#bcbcbc')
            
        textFont(font)
        textSize(50)
        text('Annuleer', 74, 75)
        
        fill('#bcbcbc')
        
        if self.current_category == 'Standaard':
            text('Categorie: ' + self.current_category, 710, 70)
        elif self.current_category == 'Kennis':
            text('Categorie: ' + self.current_category, 820, 70)
        else:
            text('Categorie: ' + self.current_category, 710, 70)
    
        textSize(40)
        textFont(font)
        text(self.question[0]['question'], 70, 150, 1000, 300)
        
        CategoryQuestion.check(self)
    
    #Bereidt de vraag voor de speler.
    def prepare_question(self, category):
        self.current_category = category
        questions_from_category = [q for q in questions if q['category'] == category.lower() and q['level'] == 'makkelijk']
        
        random_index = random.randint(0, 39)
        self.question = [question for index, question  in enumerate(questions_from_category) if index == random_index]
    
    #Zorgt dat hoveren over knoppen wordt bijgehouden.
    def check(self):
        CategoryQuestion.mouse_over(self)
    
    #Houdt bij of er met de muis is bewogen over locaties.
    def mouse_over(self):
        if (60 <= mouseX <= 310) and (20 <= mouseY <= 100):
            self.hovered_cancel = True
        else:
            self.hovered_cancel = False
            
    def mousePressed(self):
        if (60 <= mouseX <= 310) and (20 <= mouseY <= 100):
            Router.set_screen('Category')
        
