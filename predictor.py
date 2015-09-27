# make predictions given images

from clarifai_basic import ClarifaiCustomModel
import json


with open('select_categories.json') as json_file:
	data = json.load(json_file)


# predict whether bubble tea or not
def predict(url):
    concept = ClarifaiCustomModel()
    highscore = 0

    for datum in data:
    	score = concept.predict(url, datum['alias'])['urls'][0]['score']
    	if score > .9:
    		return datum 
    	if score > highscore and score > 0.6:
    		category = datum
    		highscore = score
    		print category['alias']
    		print score
    return category