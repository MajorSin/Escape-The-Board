import json
import random

used_makkelijk = []

#VRAAG AAN TEGENSTANDER
class tegenstander():
    def vraag(self, category):
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
                if main['level'] == "makkelijk":
                    if i not in used_makkelijk:
                        index_random.append(i)
            elif main['level'] == "makkelijk" and main['category'] == category.lower():
                if i not in used_makkelijk:
                    index_random.append(i)
        try:
            index = random.choice(index_random)
            main = data[index]
        except:
            main = 'empty'
        return main
    
    def antwoord(self):
        used_makkelijk.append(index)
