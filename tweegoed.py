import json
import random

used_makkelijk = []

#TWEE VRAGEN
class tweeGoed():
    def vraagEen(self, category):
        global main
        global index
        textFont(createFont("fonts/Bungee-Regular.ttf", 22))
        fill(250,250,250)
        index_random = []
        json_file = open('questions.json')
        data = json.loads(json_file.read())
        for i in range(len(data)):
            main = data[i]
            if category == "standaard":
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
    
    def vraagTwee(self, category):
        global main2
        global index2
        textFont(createFont("fonts/Bungee-Regular.ttf", 22))
        fill(250,250,250)
        index_random = []
        json_file = open('questions.json')
        data = json.loads(json_file.read())
        for i in range(len(data)):
            main2 = data[i]
            if category == "standaard":
                if main2['level'] == "makkelijk":
                    if i not in used_makkelijk:
                        index_random.append(i)
            elif main2['level'] == "makkelijk" and main2['category'] == category.lower():
                if i not in used_makkelijk:
                    index_random.append(i)
        try:
            index2 = random.choice(index_random)
            while index == index2:
                index2 = random.choice(index_random)
            main2 = data[index2]
        except:
            main2 = 'empty'
        return main2
    
    def antwoord(self):
        used_makkelijk.append(index)
        used_makkelijk.append(index2)
