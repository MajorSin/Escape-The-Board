class UserInput():
    pressed_enter = False
    hovering = '#ffffff'
    clicked = False 
    user_id = 0
    editing = False
    deleting = False
    found = False
    pressed = False
    current_user = 0
    
    def __init__(self, input, user_list, user):
        self.input = input
        self.user_list = user_list
        self.user = user
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        fill(50)
        stroke(self.hovering)
        strokeWeight(5)
        textSize(70)
        
        #Houdt bij wat gecheckt moet worden.
        UserInput.check(self)
    
    #Controleert de invoer, gebruikers en hover.
    def check(self):
        UserInput.check_input(self)
        UserInput.check_users(self)
        UserInput.mouse_hover(self)

    #Houdt de input in de gaten.
    def check_input(self):
        #Korte notatie van een conditie.
        characters = len(self.input) < 3 or len(self.input) > 16
        
        #Toont op basis van statussen bij het aanpassen en verwijderen.
        if not(self.deleting) and not(self.editing):
            rect(200, 250, 600, 100)
            fill(255)
            text(self.input, 220, 325)
        elif self.editing and not(self.found):
            fill(255)
            textSize(50)
            text('Druk het spelernummers in \ndie je wilt aanpassen', 198, 280)
        elif self.editing and self.found and self.pressed:
            rect(200, 250, 600, 100)
            fill(255)    
            text(self.input, 220, 325)
        elif self.deleting:
            fill(255)
            textSize(50)
            text('Druk het spelernummers in \nom de speler te verwijderen', 198, 280)
        
        #Als er geklikt wordt op de input, dan wordt dit getoond.
        if self.clicked == False and not(self.input) and not(self.deleting or self.editing):
            fill(self.hovering)
            textSize(45)
            text('Klik om speler toe te voegen', 218, 318)
        elif self.clicked == False and not(self.input) and (self.editing and self.found):
            fill(self.hovering)
            textSize(44)
            text('Klik om speler aan te passen', 218, 318)
            
        #Houdt de volgende errors hieronder bij.
        if not(self.deleting):
            if not(self.input) and (self.pressed_enter and self.clicked):
                error = UserInput.get_error(self, 'Voer een naam in', 223, 180)
            if len(self.user_list.users) == 4 and self.pressed_enter and not(characters):
                error = UserInput.get_error(self, 'Maximaal 4 spelers', 185, 180)
            elif characters and (self.pressed_enter and self.input):
                if len(self.input) < 3:
                    error = UserInput.get_error(self, 'Minimaal 3 karakters', 140, 180)
                else:
                    error = UserInput.get_error(self, 'Maximaal 16 karakters', 140, 180)    
        if self.pressed and (self.editing or self.deleting) and not(self.found):
            error = UserInput.get_error(self, 'Speler bestaat niet', 194, 180)
                    
    #Zorgt dat de id van users goed wordt meegegeven.
    def check_users(self):
        if not(len(self.user_list.users) == self.user_id):
            self.user_id = len(self.user_list.users)
            
    #Toont error met de layout van hieronder.
    def get_error(self, name, x, y):
        font = createFont("fonts/monster-pumpkin.ttf", 80);
        fill('#771414')
        textFont(font);
        text(name, x, y)

    #Houdt bij of er met de muis is bewogen over locaties.
    def mouse_hover(self):
        #Houdt muis hover bij en past de kleur aan.
        if (200 <= mouseX <= 800) and (250 <= mouseY <= 350):
            self.hovering = '#00f1fe'
        else:
            self.hovering = '#ffffff'
    
    #Schakelt de status van aanpassen aan en uit.
    def enable_editing(self):
        if self.editing == True:
            self.editing = False
        else:
            self.editing = True
            
        self.pressed_enter = False
        self.found = False
        self.pressed = False
        self.clicked = False
    
    #Schakelt de status van verwijderen aan en uit.
    def enable_deleting(self):
        if self.deleting == True:
            self.deleting = False
        else:
            self.deleting = True
        
        self.found = False
        self.pressed_enter = False
        self.pressed = False
        self.clicked = False

    def keyPressed(self):
        #Korte notatie van een van de condities.
        characters = len(self.input) < 3 or len(self.input) > 16
        
        #Controleert wat de gebruiker indrukt.
        if self.clicked == True:
            if ('A' <= key >= 'Z') and not(key == ' '):
                self.pressed_enter = False
                if not(self.input):
                    self.input += key.capitalize()
                else:
                    self.input += key
            elif key == BACKSPACE:
                self.input = self.input[:-1]
            elif key == ENTER and not(self.input):
                self.pressed_enter = True
            elif key == ENTER and self.input:
                self.pressed_enter = True
                if not(self.editing):
                    if len(self.user_list.users) < 4 and not(characters):
                        if len(self.user_list.users) == 0:
                            self.user_id = 0
                        self.user_id = self.user_id + 1    
                        user = self.user(self.user_id, self.input, 0)
                        self.user_list.add_user(user)
                        self.pressed_enter = False
                        self.user_id = self.user_id
                        self.input = ''
                        self.clicked = False
                elif not(characters):
                    self.user_list.edit_user(self.current_user, self.input)
                    self.editing = False
                    self.pressed_enter = False
                    self.input = ''
                    self.clicked = False
                    
        #Voert uit als aanpassen of verwijderen aan staat.
        if self.editing:
            if '1' <= key <= '4':
                for user in self.user_list.users:
                    if user.id == int(key):
                        self.found = True
                        self.pressed = True
                        self.current_user = user.id
                        break
                    else:
                        self.found = False
                        self.pressed = True
        elif self.deleting:
            if '1' <= key <= '4':
                for user in self.user_list.users:
                    if user.id == int(key):
                        self.user_list.delete_user(int(key))
                        self.deleting = False
                        self.found = True
                        self.pressed = True
                    else:
                        self.found = False
                        self.pressed = True
            
    def mousePressed(self):
        if (200 <= mouseX <= 800) and (250 <= mouseY <= 350):
            self.clicked = True
        else:
            self.clicked = False
            
