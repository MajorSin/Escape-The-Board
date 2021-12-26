class Leaderboard():    
    def __init__(self, user_list, current_user):
        self.current_user = current_user
        self.user_list = user_list
    
    #Gereed stellen wat nodig is.
    def prep(self):
        global leaderboard_image
        leaderboard_image = loadImage("images/leaderboard.png")
        leaderboard_image.resize(170, 170)
        
        global font
        font = createFont('Segoe UI Bold', 70)
        
        global user_font
        user_font = createFont('Segoe UI Bold', 50)
        
        global right_arrow
        right_arrow = loadImage("images/right-arrow.png")
        right_arrow.resize(50, 50)
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        fill(0)
        rect(800, 0, 480, 280)
        
        fill('#00f1fe')
        circle(1040, 100, 140)
        image(leaderboard_image, 953, 10)
        
        textFont(font)
        textSize(60)
        text('LEADERBOARD', 825, 250)
        
        fill(40, 64, 66, 120)
        rect(800, 290, 480, 430)
        
        self.user_list = sorted(self.user_list, key= lambda x: x.score, reverse = True)
                
        temp = 380
        for user in self.user_list:
            textFont(user_font)
            if user.id == 1:
                fill('#D26466')
            elif user.id == 2:
                fill('#A7C7E7')
            elif user.id == 3:
                fill('#77dd77')
            else:
                fill('#FDFD96')
         
            if user.id == self.current_user:
                image(right_arrow, 840, temp - 40)
                text(str(user.id) + '. ' + str(user.name), 900, temp)
            else:
                text(str(user.id) + '. ' + str(user.name), 850, temp)
            text(str(user.score), 1200, temp)
            temp += 90
            
    def next_user(self):
        if self.current_user == len(self.user_list):
            self.current_user = 1
        else:
            self.current_user += 1
        for user in self.user_list:
            if user.id == self.current_user:
                if user.jailed == True:
                    if self.current_user == len(self.user_list):
                        self.current_user = 1
                        for user2 in self.user_list:
                            if user2.id == self.current_user:
                                if user2.jailed == True:
                                    self.current_user += 1
                                    user2.jailed = False
                    else:
                        self.current_user += 1
                user.jailed = False
                        
                    
    def increment_score(self):
        for user in self.user_list:
            if user.id == self.current_user:
                user.score += 1
