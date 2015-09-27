# script to train custom model with food categories from yelp's categories 
# list

from clarifai_basic import ClarifaiCustomModel
import json
import pprint
import bing
import random

MAIN_GROUPS = ("restaurants", "food", "gourmet")
EXCEPTIONS = ("congee", "dimsum", "donburi", "ramen")
# DONE = ("afghani", "african", "arabian", "armenian", "argentine", "asianfusion",
#     "asturian", "australian", "austrian", "bagels", "baguettes", "bakeries", 
#     "bangladeshi", "basque", "bavarian", "bbq", "beer_and_wine", "beergarden", 
#     "beerhall", "beisl", "belgian", "beverage_stores", "bistros", "blacksea", 
#     "brasseries", "brazilian", "breakfast_brunch", "breweries", "british", 
#     "bubbletea", "buffets", "bulgarian", "burgers", "burmese", "butcher", "cafes",
#     "cafeteria", "cajun", "cakeshop", "cambodian", "candy", "canteen", "caribbean")

with open('categories.json') as json_file:
    data = json.load(json_file)

categories = []

for d in data:
    # ignore non-food data
    if d['parents'][0] not in MAIN_GROUPS and d['alias'] not in EXCEPTIONS:
        continue
    # add 'food' to restaurants for better search optimization
    if d['parents'][0] in MAIN_GROUPS[0]:
        d['title'] = str(d['title']) + ' Food'

    categories.append({
        'alias': str(d['alias']),
        'title': str(d['title'])
    })

# pprint.pprint(categories)

concept = ClarifaiCustomModel()

train model for each category
for cat in categories:
    print cat['alias']
    if cat['alias'] in DONE:
        continue

    # get images to train with
    images = bing.image_search(query=cat['title'])
    for image in images:
        print image
        print images.index(image)
        concept.positive(image, cat['alias'])

    # choose random food
    neg_index = random.randint(0, len(categories)-1)
    while neg_index == categories.index(cat):
        neg_index = random.randint(0, len(categories)-1)
    # find negative examples
    neg_images = bing.image_search(query=categories[neg_index]['title'])

    for image in neg_images:
        print image
        print neg_images.index(image)
        concept.negative(image, cat['alias'])

    concept.train(cat['alias'])

    # print('\n\n' + cat['alias'])
