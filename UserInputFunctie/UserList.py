class UserList():
    def __init__(self, users):
        self.users = users
    
    def display(self):
        users = self.users
        
        fill(255)
        stroke(255)
        textSize(50)
        text('Spelers:', 192, 500)
        line(198, 530, 798, 530);
        
        if users:
            textSize(40)
            temp = 600
            for user in users:
                text(user, 192, temp)
                temp += 50
        
    def add_user(self, user):
        users = self.users
        users.append('Speler ' + str(len(users) + 1) + ': ' + user)
            
        
        
