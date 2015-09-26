# make predictions given images

from clarifai_basic import ClarifaiCustomModel

# predict whether bubble tea or not
def predict(url):
    concept = ClarifaiCustomModel()
    result = concept.predict(url, 'bubbletea')

    if result['urls'][0]['score'] >= .5:
        return True
    else:
        return False
