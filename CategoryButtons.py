import Router

class CategoryButtons():
    standard = 30
    knowledge = 30
    math = 30
    hovered_return = False
    
    #Gereed stellen wat nodig is.
    def prep(self):
        global title_background
        title_background = loadImage("images/title-background.png")
        
        global title_font
        title_font = createFont("fonts/forresta.otf", 130)
        
        global buttons_font
        buttons_font = createFont("fonts/evil-empire.otf", 80)
        
        global return_image
        return_image = loadImage("images/left-arrow.png")
        return_image.resize(110, 128)
        
        global return_image_hovered
        return_image_hovered = loadImage("images/left-arrow-hovered.png")
        return_image_hovered.resize(110, 128)
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        fill(100)
        stroke(100)
        rect(40, 40, 150, 120, 15)
        
        #Hover van de terug knop.
        if self.hovered_return:
            image(return_image_hovered, 60, 40)
        else:
            image(return_image, 60, 40)
            
        #Titel achtergrond.
        image(title_background, 300, 60, 680, 120)
        
        #Toegepaste titel font.
        fill('#bcbcbc')
        textFont(title_font);
        text('Kies categorie', 335, 150)
        
        #Toegepaste knoppen font.
        textSize(110)
        textFont(buttons_font)
        strokeWeight(5)
        
        #Standaard categorie (kennis & wiskunde).
        fill(self.standard)
        stroke(self.standard)
        rect(350, 250, 580, 110)
        fill(255)
        text('Standaard', 570, 335)
        
        #Kennis categorie.
        fill(self.knowledge)
        stroke(self.knowledge)
        rect(350, 400, 580, 110)
        fill(255)
        text('Kennis', 690, 485)
                
        #Wiskunde categorie.
        fill(self.math)
        stroke(self.math)
        rect(350, 550, 580, 110)
        fill(255)
        text('Wiskunde', 590, 635)
            
        #Houdt bij wat gecheckt moet worden.
        CategoryButtons.check(self)
        
    #Zorgt dat hoveren over knoppen wordt bijgehouden.
    def check(self):
        CategoryButtons.mouse_over(self)

    #Houdt bij of er met de muis is bewogen over locaties.
    def mouse_over(self):
        mouse_x = 350 <= mouseX <= 930
        
        #Locatie op de x en y van de knoppen.
        standard_l = mouse_x and (250 <= mouseY <= 360)
        knowledge_l = mouse_x and (400 <= mouseY <= 510)
        math_l = mouse_x and (550 <= mouseY <= 660)
        
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
            
        if (40 <= mouseX <= 190) and (40 <= mouseY <= 160):
            self.hovered_return = True
        else:
            self.hovered_return = False
    
    def mousePressed(self):
        mouse_x = 350 <= mouseX <= 930
        
        #Locatie op de x en y van de knoppen.
        standard_l = mouse_x and (250 <= mouseY <= 360)
        knowledge_l = mouse_x and (400 <= mouseY <= 510)
        math_l = mouse_x and (550 <= mouseY <= 660)
        
        #Zorgt dat functies worden uitgevoert als een knop is geklikt.
        if (standard_l or knowledge_l or math_l) and Router.current_screen == 'Categories':
            if standard_l:
                Router.set_screen('Standard')
            elif knowledge_l:
                Router.set_screen('Knowledge')
            else:
                Router.set_screen('Math')
            
