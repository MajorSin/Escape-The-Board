class UserInput():
    pressed_enter = False
    hovering = '#ffffff'
    clicked = False 
    user_id = 0
    editing = False
    deleting = False
    found = False
    pressed = False
    already_exists = False
    current_user = 0
    
    def __init__(self, input, user_list, user):
        self.input = input
        self.user_list = user_list
        self.user = user
        
    #Gereed stellen wat nodig is
    def prep(self):
        #Laadt de afbeelding van de cursor in.
        global error_font
        error_font = createFont("fonts/monster-pumpkin.ttf", 70);
        
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
        characters = len(self.input) < 3
        
        #Toont op basis van statussen bij het aanpassen en verwijderen.
        if not(self.deleting) and not(self.editing):
            rect(120, 340, 600, 100)
            fill(255)
            text(self.input, 145, 414)
        elif self.editing and not(self.found):
            fill(255)
            textSize(50)
            text('Druk het spelernummers in \ndie je wilt aanpassen', 120, 380)
        elif self.editing and self.found and self.pressed:
            rect(120, 340, 600, 100)
            fill(255)    
            text(self.input, 145, 414)
        elif self.deleting:
            fill(255)
            textSize(50)
            text('Druk het spelernummers in \nom de speler te verwijderen', 120, 380)
        
        #Als er geklikt wordt op de input, dan wordt dit getoond.
        if self.clicked == False and not(self.input) and not(self.deleting or self.editing):
            fill(self.hovering)
            textSize(45)
            text('Klik om speler toe te voegen', 137, 405)
        elif self.clicked == False and not(self.input) and (self.editing and self.found):
            fill(self.hovering)
            textSize(44)
            text('Klik om speler' + str(self.current_user) + 'aan te passen', 137, 405)
            
        #Houdt de volgende errors hieronder bij.
        if not(self.deleting):
            if not(self.input) and (self.pressed_enter and self.clicked):
                error = UserInput.get_error(self, 'Voer een naam in', 175, 300)
            if len(self.user_list.users) == 4 and self.pressed_enter and (not(characters) and not(self.editing)):
                error = UserInput.get_error(self, 'Maximaal 4 spelers', 140, 300)
            if characters and (self.pressed_enter and self.input):
                if len(self.input) < 3:
                    error = UserInput.get_error(self, 'Minimaal 3 karakters', 100, 300)
                    
        if self.pressed and (self.editing or self.deleting) and not(self.found):
            error = UserInput.get_error(self, 'Speler ' + str(self.current_user) + ' bestaat niet', 120, 300)
        
        if self.already_exists == True and not(characters) and self.pressed_enter:
            error = UserInput.get_error(self, 'Speler bestaat al', 175, 300)
                    
    #Zorgt dat de id van users goed wordt meegegeven.
    def check_users(self):
        if not(len(self.user_list.users) == self.user_id):
            self.user_id = len(self.user_list.users)
            
    #Toont error met de layout van hieronder.
    def get_error(self, name, x, y):
        fill('#b72222') #b72222 #771414
        textFont(error_font);
        text(name, x, y)

    #Houdt bij of er met de muis is bewogen over locaties.
    def mouse_hover(self):
        #Houdt muis hover bij en past de kleur aan.
        if (120 <= mouseX <= 720) and (340 <= mouseY <= 440):
            self.hovering = '#00f1fe'
        else:
            self.hovering = '#ffffff'
    
    #Schakelt de status van aanpassen aan en uit.
    def enable_editing(self):
        if self.editing == True:
            self.editing = False
            self.user_list.set_user(0)
        else:
            self.editing = True
            
        self.pressed_enter = False
        self.found = False
        self.pressed = False
        self.clicked = False
        self.input = ''
    
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
        self.input = ''

    def keyPressed(self):
        #Korte notatie van een van de condities.
        characters = len(self.input) < 3
        
        #Controleert wat de gebruiker indrukt.
        if self.clicked == True:
            if ('A' <= key >= 'Z') and not(key == ' ' or key == DELETE):
                self.pressed_enter = False
                if not(self.input):
                    self.input += key.capitalize()
                else:
                    if len(self.input) < 10:
                        self.input += key
            elif key == BACKSPACE:
                self.input = self.input[:-1]
                self.pressed_enter = False
            elif key == ENTER and not(self.input):
                self.pressed_enter = True
            elif key == ENTER and self.input:
                self.pressed_enter = True
                for user in self.user_list.users:
                    if user.name == self.input:
                        if self.editing and self.current_user == user.id:
                            self.already_exists = False
                            break
                        else:
                            self.already_exists = True
                            break
                    else:
                        self.already_exists = False
                if not(self.already_exists):        
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
                    elif self.editing and not(characters):
                        self.user_list.edit_user(self.current_user, self.input)
                        self.found = False
                        self.pressed_enter = False
                        self.pressed = False
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
                        self.user_list.set_user(self.current_user)
                        self.input = user.name
                        break
                    else:
                        self.found = False
                        self.pressed = True
                        self.current_user = int(key)
        elif self.deleting:
            if '1' <= key <= '4':
                for user in self.user_list.users:
                    if user.id == int(key):
                        deletion = self.user_list.delete_user(int(key))
                        if deletion == 'Empty':
                            UserInput.enable_deleting(self)
                        self.found = True
                        self.pressed = True
                        self.current_user = int(key)
                        break
                    else:
                        self.found = False
                        self.pressed = True
                        self.current_user = int(key) 
                                    
    def mousePressed(self):
        if (120 <= mouseX <= 720) and (340 <= mouseY <= 440):
            self.clicked = True
        else:
            self.clicked = False
            self.pressed_enter = False
