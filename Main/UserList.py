class UserList():
    current_user = 0
    
    def __init__(self, users):
        self.users = users
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        fill(255)
        stroke(255)
        textSize(50)
        text('Spelers:', 830, 300)
        line(1200, 340, 835, 340);
        
        #Toont de gebruikers die zijn toegevoegd.
        if self.users:
            textSize(40)
            temp = 400
            for user in self.users:
                if user.id == self.current_user:
                    fill('#00f1fe')
                else:
                    fill(255)
                    
                text(str(user.id) + ': ' + str(user.name), 830, temp)
                temp += 60
         
    #Voegt een nieuwe gebruiker toe.
    def add_user(self, user):
        user = user
        self.users.append(user)
    
    #Past een gebruiker aan.
    def edit_user(self, user_id, name):
        user = user_id
        for index in self.users:
            if index.id == user:
                index.name = name 
                UserList.set_user(self, 0)
                break
    
    def set_user(self, user_id):
        self.current_user = user_id
        
    #Verwijdert een gebruiker.
    def delete_user(self, user_id):
        user = user_id
        
        for index in self.users:
            if index.id == user:
                self.users.remove(index)
        
        if self.users:
            temp = 1
            for user in self.users:
                user.id = temp
                temp += 1
        else:
            return 'Empty'
        
    #Maakt de lijst met gebruikers leeg.
    def reset_list(self):
        self.users = []
    
    def reset_players(self):
        for user in self.users:
            user.score = 0
            user.jailed = False
