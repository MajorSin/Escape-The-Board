import Router

class CategoryButtons():
    standard = 30
    knowledge = 30
    math = 30
    
    #Gereed stellen wat nodig is.
    def prep(self):
        global title_background
        title_background = loadImage("images/title-background.png")
        
        global title_font
        title_font = createFont("fonts/forresta.otf", 130)
        
        global buttons_font
        buttons_font = createFont("fonts/american-captain.otf", 80)
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        #Titel achtergrond.
        image(title_background, 150, 120, 710, 120)
        
        #Toegepaste titel font.
        fill('#b9b8b6')
        textFont(title_font);
        text('Kies categorie', 200, 215)
    
        #Toegepaste knoppen font.
        textSize(110)
        textFont(buttons_font)
        strokeWeight(5)
        
        #Standaard categorie (kennis & wiskunde).
        fill(self.standard)
        stroke(self.standard)
        rect(250, 400, 500, 120)
        fill(255)
        text('Standaard', 420, 490)
        
        #Kennis categorie.
        fill(self.knowledge)
        stroke(self.knowledge)
        rect(250, 570, 500, 120)
        fill(255)
        text('Kennis', 545, 660)
                
        #Wiskunde categorie.
        fill(self.math)
        stroke(self.math)
        rect(250, 740, 500, 120)
        fill(255)
        text('Wiskunde', 460, 830)
            
        #Houdt bij wat gecheckt moet worden.
        CategoryButtons.check(self)
        
    #Zorgt dat hoveren over knoppen wordt bijgehouden.
    def check(self):
        CategoryButtons.mouse_over(self)

    #Houdt bij of er met de muis is bewogen over locaties.
    def mouse_over(self):
        #Locatie op de x en y van de knoppen.
        standard_l = (250 <= mouseX <= 750) and (400 <= mouseY <= 520)
        knowledge_l = (250 <= mouseX <= 750) and (570 <= mouseY <= 690)
        math_l = (250 <= mouseX <= 750) and (740 <= mouseY <= 860)
        
        #Wijzigt de kleur van de knoppen op basis van locatie.
        if (standard_l or knowledge_l or math_l):
            if standard_l:
                self.standard = '#2d42ab'
            elif knowledge_l:
                self.knowledge = '#640700'
            else:
                self.math = '#123900'
        else:
            self.standard = 100
            self.knowledge = 100 
            self.math = 100
    
    def mousePressed(self):
        #Locatie op de x en y van de knoppen.
        standard_l = (250 <= mouseX <= 750) and (400 <= mouseY <= 520)
        knowledge_l = (250 <= mouseX <= 750) and (570 <= mouseY <= 690)
        math_l = (250 <= mouseX <= 750) and (740 <= mouseY <= 860)
        
        #Zorgt dat functies worden uitgevoert als een knop is geklikt.
        if (standard_l or knowledge_l or math_l):
            if standard_l:
                Router.set_screen('Standard')
            elif knowledge_l:
                Router.set_screen('Knowledge')
            else:
                Router.set_screen('Math')
            
