class UserList():
    def __init__(self, users):
        self.users = users
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        fill(255)
        stroke(255)
        textSize(50)
        text('Spelers:', 192, 450)
        line(198, 480, 798, 480);
        
        #Toont de gebruikers die zijn toegevoegd.
        if self.users:
            textSize(40)
            temp = 550
            for user in self.users:
                text('Speler ' + str(user.id) + ': ' + str(user.name), 192, temp)
                temp += 50
         
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
                break
    
    #Verwijdert een gebruiker.
    def delete_user(self, user_id):
        user = user_id
        
        for index in self.users:
            if index.id == user:
                self.users.remove(index)
                
        temp = 1
        for user in self.users:
            user.id = temp
            temp += 1
        
    #Maakt de lijst met gebruikers leeg.
    def reset_list(self):
        self.users = []
