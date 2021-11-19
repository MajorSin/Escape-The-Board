class UserList():
    def __init__(self, users):
        self.users = users
        
    def display(self):
        users = self.users
        
        fill(255)
        stroke(255)
        textSize(50)
        text('Spelers:', 192, 450)
        line(198, 480, 798, 480);
        
        if users:
            textSize(40)
            temp = 550
            for user in users:
                text('Speler ' + str(user.id) + ': ' + str(user.name), 192, temp)
                temp += 50
         
    def add_user(self, user):
        users = self.users
        user = user
        users.append(user)
        
    def delete_user(self, user_id):
        users = self.users
        user = int(user_id)
        for index in users:
            if index.id == user:
                users.remove(index)
        temp = 1
        for user in users:
            user.id = temp
            temp += 1
        self.users = users
        
    def reset_list(self):
        users = self.users
        users = []
        self.users = users
    
                
