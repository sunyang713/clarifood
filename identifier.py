# identifies category, cuisine, or name of food from image.

from clarifai_basic import ClarifaiCustomModel
import json

with open('demo_cat.json') as json_file:
    data = json.load(json_file)

def identify(url):
    concept = ClarifaiCustomModel()
    highscore = 0
    for d in data:
    	score = concept.predict(url, d['alias'])['urls'][0]['score']
    	if score > .9:
    		return datum 
    	if score > highscore and score > 0.5:
    		category = datum
    		highscore = score
    		print category['alias']
    		print score
    return category

