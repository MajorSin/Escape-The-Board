class UserButtons():
    edit = 100
    delete = 100
    reset = 100
    
    def __init__(self, user_list, user_input):
        self.user_list = user_list
        self.user_input = user_input
    
    #Laadt alles in wat getoond moet worden.
    def display(self):
        #Laadt de afbeeldingen in.
        edit_image = loadImage('images/edit.png')
        delete_image = loadImage('images/delete.png')
        reset_image = loadImage('images/reset.png')
        
        #Status van aanpassen en verwijderen.
        editing = self.user_input.editing
        deleting = self.user_input.deleting
        
        #Toont de knoppen op basis van statussen.
        if (editing and not(deleting)) or not(editing) and not(deleting):
            fill(self.edit)
            stroke(self.edit)
            rect(198, 800, 150, 100)
            image(edit_image, 245, 820)
      
        if (deleting and not(editing)) or not(deleting) and not(editing):  
            fill(self.delete)
            stroke(self.delete)
            rect(427, 800, 150, 100)
            image(delete_image, 469, 820)
        
        if not(deleting) and not(editing):
            fill(self.reset)
            stroke(self.reset)
            rect(650, 800, 150, 100)
            image(reset_image, 694, 820)
            
        #Houdt bij wat gecheckt moet worden.
        UserButtons.check(self)
        
    #Zorgt dat hoveren over knoppen wordt bijgehouden.
    def check(self):
        UserButtons.mouse_over(self)

    #Houdt bij of er met de muis is bewogen over locaties.
    def mouse_over(self):
        #Locatie op de x en y van de knoppen.
        edit_l = 198 <= mouseX <= 348
        delete_l = 428 <= mouseX <= 578
        reset_l = 650 <= mouseX <= 800
        
        #Wijzigt de kleur van de knoppen op basis van locatie.
        if (edit_l or delete_l or reset_l) and 800 <= mouseY <= 900:
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
    
    def mousePressed(self):
        #Locatie op de x en y van de knoppen.
        edit_l = 198 <= mouseX <= 348
        delete_l = 428 <= mouseX <= 578
        reset_l = 650 <= mouseX <= 800
        
        #Zorgt dat functies worden uitgevoert als een knop is geklikt.
        if (edit_l or delete_l or reset_l) and 800 <= mouseY <= 900:
            if edit_l and not(self.user_input.deleting):
                if self.user_list.users:
                    self.user_input.enable_editing()
            elif delete_l and not(self.user_input.editing):
                if self.user_list.users:
                    self.user_input.enable_deleting()
            elif reset_l and not(self.user_input.deleting or self.user_input.editing):
                self.user_list.reset_list()
