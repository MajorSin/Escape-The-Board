import CategoryMain, json, random

class CategoryQuestion():
    question = []
    used_makkelijk = []
    current_category = ''
    hovered_cancel = False
    hovered_answer = False
    show_answer = False
    
    def __init__(self, leaderboard):
        self.leaderboard = leaderboard
        
    #Gereed stellen wat nodig is.
    def prep(self):
        global json_file
        json_file = open('data/questions.json')
        
        global questions
        questions = json.loads(json_file.read())
    
        global main_background
        main_background = loadImage("images/main-background.jpg")
        
        global font
        font = createFont('Segoe UI Bold', 40)
        
        global correct_font
        correct_font = createFont('fonts/bungee-regular.ttf', 50)
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        tint(120)
        image(main_background, 0, 0)
        
        fill(100)
        rect(60, 20, 250, 80)
        
        if self.hovered_cancel:
            fill('#00f1fe')
        else:
            fill('#bcbcbc')

        textFont(font)
        textSize(50)
        text('Annuleer', 77, 75)
        
        fill('#bcbcbc')
        
        if self.current_category == 'Standaard':
            text('Categorie: ' + self.current_category, 710, 70)
        elif self.current_category == 'Kennis':
            text('Categorie: ' + self.current_category, 820, 70)
        else:
            text('Categorie: ' + self.current_category, 710, 70)
        
        CategoryQuestion.loadQuestion(self)
        
        id = self.leaderboard.current_user
        if id == 1:
            fill('#D26466')
        elif id == 2:
            fill('#A7C7E7')
        elif id == 3:
            fill('#77dd77')
        else:
            fill('#FDFD96')
        
        users = self.leaderboard.user_list
        name = ''
        for user in users:
            if user.id == id:
                name = user.name
                
        text('Speler ' + str(self.leaderboard.current_user) + ': ' + str(name) + ' ' + 'is aan de beurt', 430, 690)
        
        CategoryQuestion.check(self)
    
    #Zorgt dat hoveren over knoppen wordt bijgehouden.
    def check(self):
        CategoryQuestion.mouse_over(self)
    
    #Houdt bij of er met de muis is bewogen over locaties.
    def mouse_over(self):

        if (60 <= mouseX <= 310) and (20 <= mouseY <= 100):
            self.hovered_cancel = True
        elif (900 <= mouseX <= 1200) and (500 <= mouseY <= 570):
            self.hovered_answer = True
        else:
            self.hovered_cancel = False
            self.hovered_answer = False
    
    #Bereidt de vraag voor de speler.
    def prepare_question(self, category):
        self.current_category = category
        
        #Hier controleert de categorie en of het antwoord eerder is gezien.
        if category == 'Standaard':
            questions_from_category = [q for q in questions if q['level'] == 'makkelijk']
            random_index = random.randint(0, 79)
            self.question = [question for index, question  in enumerate(questions_from_category) if index == random_index]
            while self.question[0] in self.used_makkelijk:
                random_index = random.randint(0, 79)
                self.question = [question for index, question  in enumerate(questions_from_category) if index == random_index]
        else:
            questions_from_category = [q for q in questions if q['category'] == category.lower() and q['level'] == 'makkelijk']
            random_index = random.randint(0, 39)
            self.question = [question for index, question  in enumerate(questions_from_category) if index == random_index]
            while self.question in self.used_makkelijk:
                random_index = random.randint(0, 39)
                self.question = [question for index, question  in enumerate(questions_from_category) if index == random_index]
    
    #Toont de vraag die bereidt was.
    def loadQuestion(self):
        textSize(40)
        textFont(font)
        text(self.question[0]['question'], 70, 150, 1100, 300)
        textSize(50)
        
        #Controleert of de vraag multiple choice is.
        if self.question[0]['type'] == 'mtp':
            if int(textWidth(self.question[0]['question'])) > 1400:
                fill('#f56600')
                circle(105, 340, 80)
                circle(500, 340, 80)
                circle(900, 340, 80)
                fill(255)
                text('A', 88, 355)
                text('B', 485, 356)
                text('C', 883, 356)
                textSize(30)
                text(str(self.question[0]['A']), 150, 320, 200, 50)
                text(str(self.question[0]['B']), 547, 320, 200, 50)
                text(str(self.question[0]['C']), 945, 320, 200, 50)
            
                textFont(font)
                textSize(30)
                
                if self.show_answer:
                    fill(255)
                    text('Antwoord: ' + str(self.question[0]['answer']), 73, 455)
            else:
                fill('#f56600')
                circle(105, 270, 80)
                circle(500, 270, 80)
                circle(900, 270, 80)
                fill(255)
                text('A', 88, 285)
                text('B', 485, 286)
                text('C', 883, 286)
                textSize(30)
                text(str(self.question[0]['A']), 150, 250, 200, 50)
                text(str(self.question[0]['B']), 547, 250, 200, 50)
                text(str(self.question[0]['C']), 945, 250, 200, 50)
        
                textFont(font)
                textSize(30)
                
                if self.show_answer:
                    fill(255)
                    text('Antwoord: ' + str(self.question[0]['answer']), 73, 385)
        else:
            #Als de text te lang is, dan krijg je andere waardes.
            if int(textWidth(self.question[0]['question'])) > 1400:
                textFont(font)
                textSize(30)
        
                if self.show_answer:
                    fill(255)
                    text('Antwoord: ' + str(self.question[0]['answer']), 73, 355)
            else: 
                textFont(font)
                textSize(30)
                
                if self.show_answer:
                    fill(255)
                    text('Antwoord: ' + str(self.question[0]['answer']), 73, 305)
                    
        if self.show_answer:
            fill('#00a023')
            rect(70, 480, 300, 150)
            fill(0)
            textFont(correct_font)
            text('VRAAG \n  GOED', 127, 543)
        
        fill(100)
        rect(900, 500, 300, 70)  
             
        if self.hovered_answer:
            fill('#00f1fe')
        else:
            fill('#bcbcbc')
        
        textFont(font)
        textSize(30)
        text('Laat antwoord zien', 915, 545)
        
    def mousePressed(self):        
        #Zorgt dat functies worden uitgevoert als een knop is geklikt.
        if (60 <= mouseX <= 310) and (20 <= mouseY <= 100):
            self.show_answer = False
            self.leaderboard.next_user()
            CategoryMain.set_screen('Category')
        elif (900 <= mouseX <= 1200) and (500 <= mouseY <= 570):
            self.show_answer = True
            self.used_makkelijk.append(self.question[0])
        elif (70 <= mouseX <= 370) and (480 <= mouseY <= 630):
            self.show_answer = False
            self.leaderboard.increment_score()
            self.leaderboard.next_user()
            CategoryMain.set_screen('Category')
        
