import Router, CategoryMain

class UserButtons():
    edit = 100
    delete = 100
    reset = 100
    hovered_return = False
    hovered_continue = False
    
    def __init__(self, user_list, user_input):
        self.user_list = user_list
        self.user_input = user_input
    
    def prep(self):
        #Laadt de afbeeldingen in.
        global edit_image
        global delete_image
        global reset_image
        
        edit_image = loadImage('images/edit.png')
        delete_image = loadImage('images/delete.png')
        reset_image = loadImage('images/reset.png')
        
        global font
        font = createFont('Arial', 70)
        
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
        #Titel achtergrond.
        image(title_background, 300, 60, 680, 120)
        
        #Toegepaste titel font.
        fill('#bcbcbc')
        textFont(title_font);
        text('Maak speler', 370, 150)
        
        fill(100)
        stroke(100)
        rect(40, 40, 150, 120, 15)
        
        #Hover van de terug knop.
        if self.hovered_return:
            image(return_image_hovered, 60, 40)
        else:
            image(return_image, 60, 40)
        
        #Knop om verder te gaan.
        if (len(self.user_list.users) >= 2) and not(self.user_input.deleting or self.user_input.editing):
            fill(100)
            stroke(100)
            rect(1040, 610, 200, 80)
            
            if self.hovered_continue:
                fill('#00f1fe')
            else:
                fill(255)
                
            textFont(buttons_font);
            textSize(60)
            text('Verder', 1063, 670)
        
        #Status van aanpassen en verwijderen.
        editing = self.user_input.editing
        deleting = self.user_input.deleting
        
        #Toont de knoppen op basis van statussen.
        if (editing and not(deleting)) or not(editing) and not(deleting):
            fill(self.edit)
            stroke(self.edit)
            rect(118, 520, 150, 100)
            image(edit_image, 165, 540)
      
        if (deleting and not(editing)) or not(deleting) and not(editing):  
            fill(self.delete)
            stroke(self.delete)
            rect(345, 520, 150, 100)
            image(delete_image, 392, 540)
        
        if not(deleting) and not(editing):
            fill(self.reset)
            stroke(self.reset)
            rect(570, 520, 150, 100)
            image(reset_image, 616, 540)
            
        #Houdt bij wat gecheckt moet worden.
        UserButtons.check(self)
        
    #Zorgt dat hoveren over knoppen wordt bijgehouden.
    def check(self):
        UserButtons.mouse_over(self)

    #Houdt bij of er met de muis is bewogen over locaties.
    def mouse_over(self):
        #Locatie op de x en y van de knoppen.
        edit_l = 118 <= mouseX <= 268
        delete_l = 345 <= mouseX <= 495
        reset_l = 570 <= mouseX <= 720
        
        #Wijzigt de kleur van de knoppen op basis van locatie.
        if (edit_l or delete_l or reset_l) and (520 <= mouseY <= 620):
            if edit_l:
                self.edit = '#2d42ab'
            elif delete_l:
                self.delete = '#640700'
            else:
                self.reset = '#123900'
        else:
            self.edit = 100
            self.delete = 100 
            self.reset = 100
    
        if (40 <= mouseX <= 190) and (40 <= mouseY <= 160):
            self.hovered_return = True
        else:
            self.hovered_return = False
            
        if (1040 <= mouseX <= 1240) and (610 <= mouseY <= 690):
            self.hovered_continue = True
        else:
            self.hovered_continue = False
        
    def mousePressed(self):
        #Locatie op de x en y van de knoppen.
        edit_l = 118 <= mouseX <= 268
        delete_l = 345 <= mouseX <= 495
        reset_l = 570 <= mouseX <= 720
        return_l = (40 <= mouseX <= 190) and (40 <= mouseY <= 160)
        continue_l = (1040 <= mouseX <= 1240) and (610 <= mouseY <= 690)
        
        #Zorgt dat functies worden uitgevoert als een knop is geklikt.
        if (edit_l or delete_l or reset_l) and (520 <= mouseY <= 620):
            if edit_l and not(self.user_input.deleting):
                if self.user_list.users:
                    self.user_input.enable_editing()
            elif delete_l and not(self.user_input.editing):
                if self.user_list.users:
                    self.user_input.enable_deleting()
            elif reset_l and not(self.user_input.deleting or self.user_input.editing):
                self.user_list.reset_list()
        elif return_l:
            Router.set_screen('InterfaceMain')
        elif continue_l:
            if len(self.user_list.users) >= 2 and Router.current_screen == 'UserInputMain':
                Router.set_screen('CategoryMain')
                CategoryMain.set_leaderboard(self.user_list.users)
            
