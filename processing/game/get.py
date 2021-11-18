#SETUP
import json

#GET DATA FROM JSON
json_file = open('questions.json')
list = json.loads(json_file.read())
