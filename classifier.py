# classifies an image with category, cuisine, or name of food.

from clarifai_basic import ClarifaiCustomModel
import json

with open('demo_categories.json') as json_file:
    data = json.load(json_file)

def classify(url):
    concept = ClarifaiCustomModel()
    highscore = 0
    classification = None
    for d in data:
    	score = concept.predict(url, d['alias'])['urls'][0]['score']
    	if score > .9:
    		return d
    	if score > highscore and score > 0.5:
    		classification = d
    		highscore = score
    		print classification['alias']
    		print score
    return classification

