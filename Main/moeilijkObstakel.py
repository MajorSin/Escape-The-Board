import json
import random

used_moeilijk = []

#MOEILIJKE VRAAG OBSTAKEL
class moeilijkObstakel():
    def inhoud(self, category):
        global main
        global index
        textFont(createFont("fonts/bungee-regular.ttf", 22))
        fill(250,250,250)
        index_random = []
        json_file = open('data/questions.json')
        data = json.loads(json_file.read())
        for i in range(len(data)):
            main = data[i]
            if category.lower() == "standaard":
                if main['level'] == "moeilijk":
                    if i not in used_moeilijk:
                        index_random.append(i)
            elif main['level'] == "moeilijk" and main['category'] == category.lower():
                if i not in used_moeilijk:
                    index_random.append(i)
        try:
            index = random.choice(index_random)
            main = data[index]
        except:
            main = 'empty'
        return main
    
    def antwoord(self):
        used_moeilijk.append(index)
